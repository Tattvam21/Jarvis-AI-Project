# Jarvis-AI-Project
A Python-based voice assistant that uses speech recognition and Google's Gemini API to answer questions, open websites, and more.



# 🎙️ Jarvis – Voice Controlled AI Assistant with Gemini API

Jarvis is a simple yet powerful voice-controlled AI assistant built in Python. It can:

- Open websites like Google, YouTube, LinkedIn  
- Play songs from your custom library  
- Read the latest news  
- Answer any question using Google's Gemini 2.5 model (Generative AI)

---

## 🚀 Features

- 🎧 Wake word: Just say **"Jarvis"** to activate!
- 🌐 Web automation: Opens Google, YouTube, LinkedIn
- 🎵 Music control: Plays songs from your own `musicLibrary`
- 📰 Latest headlines: Fetches and speaks top news
- 🧠 AI answers: Uses Gemini (2.5 Flash) to answer general queries
- 🔊 Text-to-speech responses via `pyttsx3`
- 🎙️ Speech-to-text via `speech_recognition`

---

## 🛠️ Requirements

Install the dependencies using:

```bash
pip install -r requirements.txt

```

Install PyAudio for microphone access:

```bash
pip install pyaudio
```
If you face issues installing pyaudio on Windows:

```bash
pip install pipwin
pipwin install pyaudio
```
## 🔐 Setup
1. Get Gemini API Key
Visit Google AI Studio and generate your API key.

Replace the key in your script like this:
```bash
genai.configure(api_key="YOUR_API_KEY_HERE")
```
2. Create a musicLibrary.py file

This should be a dictionary mapping song names to YouTube links.

Example:

# musicLibrary.py
```bash
music = {
    "believer": "https://www.youtube.com/watch?v=7wtfhZwyrcc",
    "shapeofyou": "https://www.youtube.com/watch?v=JGwWNGJdvx8"
}
```
## 🧪 How to Run

```bash
python your_script_name.py
```
Then say:

```nginx
Jarvis
And speak your command:

Open Google

Play believer

Tell me the news

What is quantum computing?
```
