JARVIS is a Python-based voice-controlled desktop assistant powered by a locally hosted Llama 3.1 AI via Ollama. It listens to your commands, opens apps, controls your PC, fetches live data, and answers questions — all hands-free and privacy-focused.

Features

Voice Recognition — Listens via microphone using Google Speech Recognition
AI Brain — Answers questions using Llama 3.1 (8B) running locally through Ollama
App Launcher — Opens Chrome, VS Code, Notepad, Calculator, VMware, WhatsApp, and more
Web Actions — Google search, YouTube search, Wikipedia, Gmail, GitHub, Instagram, Twitter
Live Data — Real-time weather (any city) and current time/date
PC Control — Volume up/down/mute, screenshot, lock, sleep, shutdown, restart
Fun Responses — Jokes, greetings, and personalized replies


Requirements

Python 3.8+
Ollama running locally with llama3.1:8b pulled
Microphone

Python Libraries
bashpip install speechrecognition pyttsx3 requests pyautogui
pip install pyaudio

Note: If pyaudio fails on Windows, install it via:
bashpip install pipwin
pipwin install pyaudio


Setup
1. Clone or download this project
bashgit clone https://github.com/hasnayn-123/jarvischatbot
cd jarvis-assistant
2. Install dependencies
bashpip install -r requirements.txt
3. Start Ollama and pull the model
bashollama pull llama3.1:8b
ollama serve
4. Run JARVIS
bashpython jarvis.py

Usage
Just speak after JARVIS says it's listening. Some example commands:
CommandAction"Open Chrome"Launches Chrome"Open VS Code"Launches VS Code"Weather in Lahore"Fetches live weather"What time is it"Tells current time"Search Python tutorials"Google search"YouTube search lofi music"YouTube search"Take a screenshot"Saves screenshot"Volume up"Increases system volume"Lock my PC"Locks the screen"Shutdown"Shuts down in 5 seconds"Tell me a joke"Tells a programming joke"What is machine learning"AI-powered answer"Goodbye JARVIS"Exits the assistant

Project Structure
jarvis-assistant/
│
├── jarvis.py          # Main assistant script
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation

How It Works

Listen — Captures audio via microphone and converts to text using Google Speech Recognition
Process — Matches the command against built-in actions using keyword detection
Respond — Executes the action and speaks the response via pyttsx3
Fallback — Unknown commands are sent to the local Llama 3.1 model via Ollama API


Built With

SpeechRecognition
pyttsx3
Ollama
PyAutoGUI
wttr.in — Weather API


Author
Hussnain
Cybersecurity Student — UET Techslab

License
This project is open-source and free to use for personal and educational purposes.
