# 🎙️ Jarvis AI Voice Assistant

An AI-powered desktop voice assistant built with Python, inspired by **J.A.R.V.I.S.** from Iron Man.

Jarvis combines real-time speech recognition, intelligent command execution, and Google's Gemini AI to create a fast, responsive voice-controlled desktop assistant. It can open websites, play music, fetch live news headlines, answer questions, and interact naturally through voice.

---

## ✨ Features

### 🚀 One-Shot Command Execution

Issue your wake word and command in a single sentence for instant responses.

**Example:**

```text
"Jarvis, open YouTube"
"Jarvis, play Believer"
"Jarvis, explain recursion"
```

No waiting for a secondary prompt.

---

### 🎤 Real-Time Speech Recognition

Uses Google's Speech Recognition engine to accurately process spoken commands with minimal latency.

---

### 🤖 AI-Powered Conversations

Powered by Google's **Gemini 2.5 Flash Lite** model, providing:

* Fast responses
* Context-aware answers
* Smart explanations
* Natural interactions

---

### 🔊 Dynamic Noise Calibration

Automatically samples ambient noise in approximately **0.5 seconds** and adjusts microphone sensitivity to improve recognition accuracy.

---

### 🌐 Web Automation

Open frequently used websites through simple voice commands.

Examples:

* Open YouTube
* Open Google
* Open GitHub
* Open LinkedIn

---

### 🎵 Music Playback

Play songs directly from your local music library using custom voice triggers.

---

### 📰 Live News Headlines

Fetches and reads the latest headlines using the NewsAPI service.

---

## 🛠️ Tech Stack

### Language

* Python 3.13

### Libraries & Frameworks

| Package           | Purpose                             |
| ----------------- | ----------------------------------- |
| SpeechRecognition | Audio capture and speech processing |
| google-genai      | Google Gemini SDK                   |
| pygame-ce         | Fast audio playback                 |
| gTTS              | Online text-to-speech               |
| pyttsx3           | Offline text-to-speech              |
| requests          | API communication                   |
| python-dotenv     | Environment variable management     |

### APIs Used

* Google Gemini API
* NewsAPI
* Google Speech Recognition

---

## 📂 Project Structure

```text
Jarvis-AI/
│
├── main.py
├── Music_Library.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/hamzatahir06/Jarvis-Virtual-Assistant.git

cd Jarvis-Virtual-Assistant
```

---

### 2. Create a Virtual Environment

Using Python 3.13 is strongly recommended.

#### Windows

```powershell
py -3.13 -m venv .venv

.venv\Scripts\Activate.ps1
```

---

### 3. Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key_here
NEWS_API=your_newsapi_key_here
```

### Obtain API Keys

#### Gemini API Key

1. Visit Google AI Studio
2. Create a new API key
3. Copy it into your `.env` file

#### NewsAPI Key

1. Register at NewsAPI.org
2. Generate an API key
3. Add it to your `.env` file

---

## 🎛️ Audio Configuration

The following settings are optimized for responsiveness and recognition accuracy:

```python
r.energy_threshold = 300
r.dynamic_energy_threshold = True
r.pause_threshold = 0.7

phrase_time_limit = 2.5
```

### Parameter Explanation

| Setting                  | Description                          |
| ------------------------ | ------------------------------------ |
| energy_threshold         | Ignores low-volume background sounds |
| dynamic_energy_threshold | Automatically adapts to room noise   |
| pause_threshold          | Determines when speech has ended     |
| phrase_time_limit        | Maximum recording duration           |

---

## 🎯 Supported Commands

### One-Shot Commands (Recommended)

#### Open Websites

```text
Jarvis, open YouTube
Jarvis, open GitHub
Jarvis, open Google
```

#### Play Music

```text
Jarvis, play Believer
```

#### Fetch News

```text
Jarvis, news
```

Reads the latest headlines aloud.

#### Ask Gemini AI

```text
Jarvis, explain recursion
Jarvis, what is quantum computing?
Jarvis, summarize Python decorators
```

---

## 🔄 Two-Step Fallback Mode

If you only say the wake word:

```text
User: Jarvis

Jarvis: Ya?

User: Open GitHub
```

The assistant will listen for a follow-up command within a short time window.

---

## 🛑 Stopping the Assistant

Say:

```text
Stop Jarvis
```

to safely terminate the assistant.

---

## 🔒 Security Notes

### Never Commit Sensitive Files

Your `.env` file contains private API keys and should never be uploaded to GitHub.

Create a `.gitignore` file containing:

```gitignore
.venv/
__pycache__/
.env
*.mp3
```

---

## 🚧 Future Improvements

Planned enhancements include:

* Weather information
* System control commands
* Email integration
* Smart home support
* Wake-word optimization
* GUI dashboard
* Cross-platform compatibility

---

## 📜 License

This project is licensed under the MIT License.

Feel free to fork, modify, and distribute it under the terms of the license.

---

## 👨‍💻 Author

**Hamza Tahir**

GitHub: https://github.com/hamzatahir06

Built with Python, Gemini AI, and a passion for creating intelligent voice assistants.
