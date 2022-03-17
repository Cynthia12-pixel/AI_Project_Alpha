import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
import features
import playsound
import pytube
import tkinter
import googletrans

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
        elif "youtube search" in query or "from youtube" in query:          #FEATURE 1:Youtube search any topic and suggesting and playing the first video if the user asks for it.
            features.youtubeSearch(query)
        elif "google search" in query or "from google" in query:            #FEATURE 2:Google search any topic and reading the first 5 lines related to the topic from wikipedia
           features.googleSearch(query)
        elif "launch the website" in query or "open the website" in query:  #FEATURE 3:Launching any website asked by the user
            features.websiteSearch()
        elif "play the song" in query or "play music" in query:             #FEATURE 4:Playing any music asked by the user from the device,in case if the song is not present in the device then playing it from youtube
            features.playMusic()
        elif "whatsapp message" in query:                                   #FEATURE 5:Automating the whatsapp.Delivering messege on the time given by the user to any person who is added to the contact_list dictionary.In case the person's name is not there then adding it to the contact_list and then sending the message on time
            features.whatsapp_auto()
        elif "take screenshot" in query:                                    #FEATURE 6:Taking Creenshot and saving it to the screenshots folder inside Additionals
            features.screenshot()
        elif "this video" in query:                                         #FEATURE 7: Automating the Youtube
            features.youtube_auto(query)
        elif "open the app" in query or "start the app" in query:           #FEATURE 8:Opening any app from the device
            features.openApps(query)
        elif "close the app" in query:                                      #FEATURE 9:Closing any app that is opened
            features.closeApps(query)
        elif "joke" in query or "entertain me" in query:                    #FEATURE 10:Hearing joke from Alpha
            features.jokes()
        elif "set alarm" in query:                                          #FEATURE 11:Setting Alarm
            features.alarm()
        elif "download the youtube video" in query or "youtube video download" in query or "download the video" in query:  #FEATURE 12:Downloading youtube videos and saving it to the folder named as "Youtube Videos"
            features.videoDownloader()
        elif "open translator" in query:                                    #FEATURE 12:Translating Hindi sentences to English
            features.Tran()
        elif "remember that" in query:                                      #FEATURE 13:Telling Alpha to remember some message so that she can remind me when I ask her to do so in future
            features.remember(query)
        elif "what do you remember" in query or "the reminder" in query:    #FEATURE 14:Asking Alpha to remind me the message that I once told her to remember
            features.reminder()
        elif "temperature of" in query or "temperature in" in query or "temperature at" in query:       #FEATURE 15
            features.Temp(query)
        elif "read a book" in query:
            features.bookReader()
        speak("What can I do for you?")
        query=takeCommand().lower()
    speak("thank you")
    speak('I hope you liked my service')
