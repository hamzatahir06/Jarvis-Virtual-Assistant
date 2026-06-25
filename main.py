import speech_recognition as sr
import pyttsx3, webbrowser, requests
import music_library
from google import genai
from google.genai import types
import os
import pygame
import time
from dotenv import load_dotenv
from gtts import gTTS

# Load API Key from .env file
load_dotenv()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize Recognizer
r = sr.Recognizer()

# --- MIC FINE-TUNING ---
r.energy_threshold = 300 #Loudness bar i.e: Things below this bar would be ignored
r.dynamic_energy_threshold = True #Automatically adjusts the bar according to environment noise
r.pause_threshold = 0.5  #How much should it wait after getting the command to execute

def speak(text):
    print(f"Jarvis: {text}") # Print it so you can read along
    tts = gTTS(text)
    tts.save('temp.mp3')

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    
    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
        
    pygame.mixer.music.unload()
    os.remove('temp.mp3')

def aiprocess(c):
    sys_instr = """
    You are Jarvis, a Virtual assistant and helpful AI assistant having expertise in Coding and skilled in general
    tasks like Alexa or Google Assistant tasks, but far better than them. 
    You speak with a touch of American charm. 
    Always keep your answers concise, short, and proactive. Give details only when the user explicitly asks for it.
    """
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",
            contents=c,
            config=types.GenerateContentConfig(
                system_instruction=sys_instr,
                temperature=0.7,
            )
        )
        return response.text
    except Exception as e:
        return f"AI Error: {e}"

def ProcessCommand(c: str):
    c = c.lower().strip()

    if c.startswith("open "):        
        site = c.replace("open ", "").strip()
        speak(f"Opening {site}")
        webbrowser.open(f"https://{site}.com")

    elif c.startswith("play "):
        try:
            # FIX: Captures multi-word songs safely
            song_name = c.replace("play ", "").strip()
            link = music_library.Music.get(song_name)
            if link: 
                speak(f"Playing {song_name} from your library.")
                webbrowser.open(link)
            else: 
                speak("Song not found in library.")
        except Exception as e: 
            speak("Error playing song.")

    elif "news" in c:
        API_KEY = os.getenv("NEWS_API")
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            articles = data.get('articles', [])

            print("\n--- TOP HEADLINES ---\n")
            # FIX: Only take the first 3 headlines so Jarvis doesn't talk forever
            for i, article in enumerate(articles[:3], 1):
                print(f"{i}. {article.get('title')}")
            
            speak("Here are the top three updates.")
            for article in articles[:3]:
                speak(article.get('title'))
        else:
            speak("Failed to fetch news. Please check your network connection.")
       
    else:
        # Let Gemini handle the request
        output = aiprocess(c)
        speak(output)

if __name__ == "__main__":
    try:
        with sr.Microphone() as source:
            print("Calibrating microphone for background noise...")
            r.adjust_for_ambient_noise(source, duration=0.5) # Cut calibration time in half
            speak("Systems online, boss.")

            while True:
                try:
                    print("\n....Listening....")
                    # Tight 2.5-second phrase window keeps things moving instantly
                    audio = r.listen(source, timeout=None, phrase_time_limit=2.5)
                    
                    print("....Recognizing....")
                    user_input = r.recognize_google(audio).lower().strip()
                    print(f"Heard: {user_input}")
                    
                    if "jarvis" in user_input:
                        # Check if user said the command in the same breath (e.g., "Jarvis open youtube")
                        command = user_input.split("jarvis")[-1].strip()
                        
                        if command:
                            # User said command immediately! Execute right away.
                            if "stop jarvis" in command:
                                speak("Shutting down systems. Goodbye Sir!")
                                break
                            ProcessCommand(command)
                        else:
                            # User JUST said "Jarvis", so ask for the command with a strict 2.5s window
                            speak("Ya?")
                            print("Listening for quick command (2.5s window)...")
                            audio = r.listen(source, timeout=2.5, phrase_time_limit=2.5)
                            
                            command = r.recognize_google(audio).lower().strip()
                            print(f"User Command: {command}")
                            
                            if "stop jarvis" in command:
                                speak("Shutting down systems. Goodbye Sir!")
                                break
                                
                            ProcessCommand(command)

                except (sr.UnknownValueError, sr.WaitTimeoutError):
                    # Silently ignore noise, timeouts, and mumbles to keep the loop moving fast
                    continue
                except Exception as e:
                    print(f"Error inside loop: {e}")
                    
    except (AssertionError, AttributeError, OSError):
        print("\n[CRITICAL ERROR]: Microphone not found. Check Windows Privacy Settings.")

