import speech_recognition as sr
import pyttsx3
import requests
import os
import subprocess
import webbrowser
import pyautogui
import datetime
import random

# ===== SETUP =====
engine = pyttsx3.init()
engine.setProperty('rate', 160)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(text):
    print(f"\nJARVIS: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    r.energy_threshold = 3000
    r.dynamic_energy_threshold = True
    try:
        with sr.Microphone() as source:
            print("\nListening...")
            r.adjust_for_ambient_noise(source, duration=0.5)
            audio = r.listen(source, timeout=6, phrase_time_limit=10)
        command = r.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.WaitTimeoutError:
        return ""
    except sr.UnknownValueError:
        return ""
    except Exception as e:
        print(f"Error: {e}")
        return ""

def ask_ollama(prompt):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.1:8b",
                "prompt": f"Answer in 2-3 short sentences only: {prompt}",
                "stream": False
            },
            timeout=30
        )
        answer = response.json()["response"]
        sentences = answer.split('.')
        short = '. '.join(sentences[:3]) + '.'
        return short
    except:
        return "Sorry, I could not connect to my brain. Make sure Ollama is running."

def get_news():
    try:
        response = requests.get(
            "https://newsapi.org/v2/top-headlines?country=us&apiKey=demo&pageSize=3"
        )
        articles = response.json().get("articles", [])
        if articles:
            speak("Here are the latest news headlines:")
            for i, article in enumerate(articles[:3]):
                speak(f"News {i+1}: {article['title']}")
        else:
            webbrowser.open("https://news.google.com")
            speak("Opening Google News for you")
    except:
        webbrowser.open("https://news.google.com")
        speak("Opening Google News for you")

def get_weather(city="Rawalpindi"):
    try:
        url = f"https://wttr.in/{city}?format=3"
        response = requests.get(url, timeout=5)
        speak(f"Weather in {city}: {response.text}")
    except:
        speak(f"Could not get weather. Opening weather for {city}")
        webbrowser.open(f"https://www.google.com/search?q=weather+{city}")

def get_time():
    now = datetime.datetime.now()
    time_str = now.strftime("%I:%M %p")
    speak(f"The current time is {time_str}")

def get_date():
    now = datetime.datetime.now()
    date_str = now.strftime("%A, %B %d, %Y")
    speak(f"Today is {date_str}")

def tell_joke():
    jokes = [
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "Why did the computer go to the doctor? Because it had a virus!",
        "What do you call a computer that sings? A Dell!",
        "Why do Java developers wear glasses? Because they don't C sharp!",
        "How do you comfort a JavaScript bug? You console it!"
    ]
    speak(random.choice(jokes))

def run_command(command):

    # === OPEN APPS ===
    if "open chrome" in command:
        subprocess.Popen("chrome.exe")
        speak("Opening Chrome")

    elif "open notepad" in command:
        subprocess.Popen("notepad.exe")
        speak("Opening Notepad")

    elif "open vs code" in command or "open visual studio" in command:
        subprocess.Popen("code")
        speak("Opening VS Code")

    elif "open instagram" in command:
        webbrowser.open("https://www.instagram.com")
        speak("Opening Instagram")

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        speak("Opening YouTube")

    elif "open whatsapp" in command:
        subprocess.Popen("whatsapp:")
        speak("Opening WhatsApp")

    elif "open facebook" in command:
        webbrowser.open("https://www.facebook.com")
        speak("Opening Facebook")

    elif "open twitter" in command or "open x" in command:
        webbrowser.open("https://www.twitter.com")
        speak("Opening Twitter")

    elif "open github" in command:
        webbrowser.open("https://www.github.com")
        speak("Opening GitHub")

    elif "open gmail" in command:
        webbrowser.open("https://www.gmail.com")
        speak("Opening Gmail")

    elif "open google" in command:
        webbrowser.open("https://www.google.com")
        speak("Opening Google")

    elif "open file manager" in command or "open files" in command:
        subprocess.Popen("explorer.exe")
        speak("Opening File Manager")

    elif "open task manager" in command:
        subprocess.Popen("taskmgr.exe")
        speak("Opening Task Manager")

    elif "open settings" in command:
        os.system("start ms-settings:")
        speak("Opening Settings")

    elif "open camera" in command:
        os.system("start microsoft.windows.camera:")
        speak("Opening Camera")

    elif "open calculator" in command:
        subprocess.Popen("calc.exe")
        speak("Opening Calculator")

    elif "open paint" in command:
        subprocess.Popen("mspaint.exe")
        speak("Opening Paint")

    elif "open cmd" in command or "open command prompt" in command:
        subprocess.Popen("cmd.exe")
        speak("Opening Command Prompt")

    elif "open vmware" in command:
        speak("Opening VMware Workstation")
        os.system("start vmware")

    # === SEARCH ===
    elif "search" in command:
        query = command.replace("search", "").strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query}")

    elif "youtube search" in command or "search on youtube" in command:
        query = command.replace("youtube search", "").replace("search on youtube", "").strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        speak(f"Searching YouTube for {query}")

    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        webbrowser.open(f"https://en.wikipedia.org/wiki/{query}")
        speak(f"Opening Wikipedia for {query}")

    # === NEWS & WEATHER ===
    elif "news" in command:
        get_news()

    elif "weather" in command:
        if "weather in" in command:
            city = command.replace("weather in", "").strip()
            get_weather(city)
        else:
            get_weather("Rawalpindi")

    # === TIME & DATE ===
    elif "what time" in command or "current time" in command:
        get_time()

    elif "what date" in command or "today date" in command or "what day" in command:
        get_date()

    # === SYSTEM CONTROLS ===
    elif "shutdown" in command:
        speak("Shutting down your PC in 5 seconds")
        os.system("shutdown /s /t 5")

    elif "restart" in command:
        speak("Restarting your PC in 5 seconds")
        os.system("shutdown /r /t 5")

    elif "sleep" in command:
        speak("Going to sleep")
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

    elif "lock" in command:
        speak("Locking your PC")
        os.system("rundll32.exe user32.dll,LockWorkStation")

    elif "volume up" in command:
        pyautogui.press('volumeup', presses=5)
        speak("Volume increased")

    elif "volume down" in command:
        pyautogui.press('volumedown', presses=5)
        speak("Volume decreased")

    elif "mute" in command or "unmute" in command:
        pyautogui.press('volumemute')
        speak("Done")

    elif "screenshot" in command:
        filename = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        pyautogui.screenshot(filename)
        speak(f"Screenshot saved as {filename}")

    elif "minimize" in command:
        pyautogui.hotkey('win', 'd')
        speak("Minimizing all windows")

    elif "maximize" in command:
        pyautogui.hotkey('win', 'up')
        speak("Maximizing window")

    # === FUN & GENERAL ===
    elif "joke" in command or "tell me a joke" in command:
        tell_joke()

    elif "how are you" in command:
        speak("I am doing great! Always ready to help you, Hussnain!")

    elif "what is your name" in command:
        speak("My name is JARVIS, your personal AI assistant.")

    elif "who made you" in command:
        speak("You made me Hussnain! With Python and Ollama AI.")

    elif "what can you do" in command:
        speak("I can open apps, search the web, tell you news and weather, control your PC volume, take screenshots, answer your questions, tell jokes, and much more!")

    elif "hello" in command or "hi jarvis" in command:
        greetings = [
            "Hello! How can I help you?",
            "Hi there! What can I do for you?",
            "Hey! JARVIS at your service!"
        ]
        speak(random.choice(greetings))

    elif "good morning" in command:
        speak("Good morning Hussnain! Have a productive day!")

    elif "good night" in command:
        speak("Good night Hussnain! Sweet dreams!")

    elif "thank you" in command or "thanks" in command:
        speak("You are welcome! Always here to help.")

    elif "who is" in command or "what is" in command or "how to" in command or "tell me about" in command or "explain" in command:
        speak("Let me think...")
        response = ask_ollama(command)
        speak(response)

    # === AI BRAIN FOR EVERYTHING ELSE ===
    else:
        speak("Let me think...")
        response = ask_ollama(command)
        speak(response)

# ===== MAIN =====
now = datetime.datetime.now().hour
if now < 12:
    greeting = "Good morning"
elif now < 17:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

speak(f"{greeting} Hussnain! JARVIS is online and ready. How can I help you?")

while True:
    command = listen()
    if command:
        if "exit" in command or "goodbye" in command or "bye jarvis" in command or "turn off" in command:
            speak("Goodbye Hussnain! Have a great day!")
            break
        run_command(command) 