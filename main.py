import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import google.generativeai as genai
import spotifyControl


recognizer = sr.Recognizer()
engine = pyttsx3.init('sapi5')  # 'sapi5' is best for Windows

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    genai.configure(api_key="ADD YOUR GEMINI API")
    model = genai.GenerativeModel('gemini-2.5-flash')
    chat = model.start_chat(history=[])

    try:
        response = chat.send_message(
            command + ". Please reply briefly.",
            generation_config={"max_output_tokens": 100}
        )

        # Safely check if there's valid output
        if response.candidates and response.candidates[0].content.parts:
            return response.text
        else:
            return "Sorry, I couldn't understand or respond to that."

    except Exception as e:
        print("AI Error:", repr(e))
        return "Something went wrong while processing your request."

def processCommand(c):
    c = c.lower()
    if "open google" in c:
        webbrowser.open("https://google.com")
    elif "open linkedin" in c:
        webbrowser.open("https://www.linkedin.com/")
    elif "open youtube" in c:
        webbrowser.open("https://www.youtube.com/")
    elif "news" in c:
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR API KEY")
        print("Telling news")

        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles[:5]:
                speak(article.get('title', ''))

    elif "play" in c.lower():
        song = c.lower().replace("play", "").replace("on spotify", "").strip()
        result = spotifyControl.play_song_in_browser(song)
        speak(result)

    
    else:
        output = aiProcess(c)
        speak(output)

if __name__ == "__main__":
    speak("Initializing Jarvis...")

    while True:
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=4)

            print("Recognizing...")
            word = recognizer.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = recognizer.listen(source, timeout=6, phrase_time_limit=6)
                    command = recognizer.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print("Error:", repr(e))







            