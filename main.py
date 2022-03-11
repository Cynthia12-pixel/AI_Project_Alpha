import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
import features

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)

def speak(audio):
    print(f"-->>{audio}\n")
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hr=int(datetime.datetime.now().hour)
    if hr>4 and hr<=12:
        greet="Good Morning"
    elif hr>12 and hr<=16:
        greet="Good Afternoon"
    elif hr>16 and hr<=21:
        greet="Good Evening"
    else:
        greet="Good Night"
    wish=greet+"\nI am Alpha \nHow can I help you?"
    speak(wish)

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"You Said:-{query}\n")
        return query
    except:
        speak("Please Repeat")
        quer=takeCommand()
        return quer



if __name__ == "__main__":
    wishMe()
    query=takeCommand().lower()
    while "thank you" not in query:
        if "hello"  in query:
            speak("Hello!")
        elif "youtube search" in query or "from youtube" in query:
            features.youtubeSearch(query)
        elif "google search" in query or "from google" in query:
           features.googleSearch(query)
        elif "launch the website" in query or "open the website" in query:
            features.websiteSearch()
        elif "play the song" in query or "play music" in query:
            features.playMusic()
        elif "whatsapp message" in query:
            features.whatsapp_auto()
        elif "take screenshot" in query:
            features.screenshot()

        speak("What can I do for you?")
        query=takeCommand().lower()
    speak("thank you")
    speak('I hope you liked my service')
