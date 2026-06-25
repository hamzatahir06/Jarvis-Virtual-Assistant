Jarvis AI Voice Assistant
An AI-powered desktop voice assistant built with Python, inspired by Jarvis from Iron Man. Jarvis can listen for voice commands, open websites, play music, fetch live news headlines, and answer questions using Google’s Gemini AI.

Features
One-Shot Execution: Processes your wake word and your command in the same breath for zero lag (e.g., "Jarvis, open YouTube").

Real-Time Speech Recognition: Utilizes Google Speech Recognition to process spoken inputs cleanly.

AI-Powered Conversations: Leverages the advanced gemini-2.5-flash-lite model for short, proactive, smart answers.

Dynamic Noise Calibration: Automatically samples background ambient hums in just 0.5 seconds to accurately isolate your voice.

Custom Web & Music Triggers: Easily open daily web pages or launch tracks directly from a local media library module.

Tech Stack
Language: Python 3.13 (Isolated environment to prevent global package conflicts)

Libraries & Frameworks:

SpeechRecognition (Audio capture & processing)

google-genai (Official Google Gemini SDK)

pygame-ce (Modern Community Edition for lightning-fast audio handling)

gTTS & pyttsx3 (Text-to-Speech processing)

requests & python-dotenv (API requests & secure configuration environment)

APIs Used: Google Gemini API, NewsAPI, Google Speech Recognition

Project Structure
Plaintext
Jarvis-AI/
│
├── main.py
├── Music_Library.py
├── .env
├── requirements.txt
└── README.md
Installation
1. Clone the Repository
Bash
git clone https://github.com/hamzatahir06/Jarvis-Virtual-Assistant.git
cd Jarvis-Virtual-Assistant
2. Create an Isolated Virtual Environment (Windows Only)
Force the virtual environment to hook into Python 3.13 to prevent package compilation errors:

PowerShell
py -3.13 -m venv .venv
.venv\Scripts\Activate.ps1
3. Install the Bulletproof Dependencies
PowerShell
pip install -r requirements.txt
Environment Variables
Create a file named .env in the root folder of your project and populate it with your personal API keys:

Ini, TOML
GEMINI_API_KEY=your_gemini_api_key_here
NEWS_API=your_newsapi_key_here
Gemini API Key: Obtain one for free at Google AI Studio.

NewsAPI Key: Register for an access token at NewsAPI.org.

Configuration Tuning
The assistant relies on optimized audio configurations inside main.py for snappy responses:

Python
r.energy_threshold = 300           # Minimum loudness bar to ignore distant whispers
r.dynamic_energy_threshold = True  # Auto-adjusts sensitivity based on room noise
r.pause_threshold = 0.7            # Wait threshold before compiling your command
phrase_time_limit = 2.5            # Max recording duration per stream window
Demo Flow & Supported Commands
Fast One-Shot Triggers (Recommended)
You do not have to wait for Jarvis to reply to you. Speak your request natively in one sentence:

User: "Jarvis, open YouTube" -> Launches https://youtube.com instantly.

User: "Jarvis, play believer" -> Fetches and plays the track from Music_Library.py.

User: "Jarvis, news" -> Pulls the top 3 US headlines and reads them out loud.

User: "Jarvis, explain recursion" -> Hands off the query directly to Gemini AI.

Two-Step Fallback
If you state the wake word cleanly on its own, Jarvis will poll the microphone sequentially:

User: "Jarvis"

Jarvis: "Ya?"

User (Within 2.5s window): "Open GitHub" -> Executes requested command wrapper.

To stop the assistant entirely, say: "Stop Jarvis".

Security Notes
Never upload your personal .env file to public repositories. Ensure your local workspace includes a .gitignore profile mapping the following rules:

Plaintext
.venv/
__pycache__/
.env
*.mp3
License
This project is licensed under the MIT License.