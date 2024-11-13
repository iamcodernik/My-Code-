import os
import datetime
import pyttsx3
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib

# Initialize TTS Engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish_me():
    hour = int(datetime.datetime.now().hour)
    greeting = "Good Morning!" if hour < 12 else "Good Afternoon!" if hour < 18 else "Good Evening!"
    speak(greeting)
    speak("I am Jarvis Sir. Please tell me how may I help you")

def take_command():
    # Takes microphone input and returns a string output
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except Exception as e:
        print("Could not understand audio, please repeat.")
        return "None"

def open_website(site_name):
    url = f"{site_name}.com"
    webbrowser.open(url)
    speak(f"Opening {site_name}")

def search_wikipedia(query):
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=2)
    speak("According to Wikipedia")
    print(results)
    speak(results)

def send_email(to, content):
    # Replace with your credentials securely
    email = os.getenv("EMAIL_USER")
    password = os.getenv("EMAIL_PASSWORD")
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(email, password)
        server.sendmail(email, to, content)
        server.close()
        speak("Email has been sent!")
    except Exception as e:
        print(e)
        speak("Sorry, I am not able to send this email")

if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command()
        if 'wikipedia' in query:
            search_wikipedia(query)
        elif 'open youtube' in query:
            open_website("youtube")
        elif 'play music' in query:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            speak(f"The time is {datetime.datetime.now().strftime('%H:%M:%S')}")
        # Add more elif statements for other commands
        else:
            speak("No matching command found")
