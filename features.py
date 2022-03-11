import datetime
import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
import keyboard

contact_list={"maa":"+919735148140","baba":"+918389866655","gomu":"+918436924914"}
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)

def speak(audio): #speaking function
    print(f"-->>{audio}\n")
    engine.say(audio)
    engine.runAndWait()

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

def googleSearch(query):
    speak("I have got something for you!")
    query = query.replace("google search", "")
    query = query.replace("alpha", "")
    pywhatkit.search(query)
    speak("Do you want me to read out something from wikipedia")
    ans = takeCommand().lower()
    if ans != "none":
        if "yes" in ans:
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)
        else:
            speak("Ok")

def youtubeSearch(query):
    speak("I have got something for you.")
    query = query.replace("youtube search", "")
    query = query.replace("alpha", "")
    web = "https://www.youtube.com/results?search_query=" + query
    webbrowser.open(web)
    speak("I have something more for you and I hope you will like it")
    pywhatkit.playonyt(query)
    keyboard.press('space bar')

def websiteSearch():
    speak("Tell the name of the website only")
    name = takeCommand()
    if name != "none":
        speak("Launching the website")
        web1 = "https://www." + name + ".com"
        webbrowser.open(web1)
        speak("Done")

def playMusic():
    speak("Tell the name of the song that you want me to play for you")
    music = takeCommand()
    music_path = "C:\\Songs\\" + music + ".mp3"
    try:
        os.startfile(music_path)
    except:
        speak("The song is not there in your device but I can play it from youtube")
        pywhatkit.playonyt(music)

def whatsapp_auto():
    speak("To whom do you want to send the messege?")
    name=takeCommand().lower()
    if name in contact_list.keys():
        msg=speak("Tell me the messege that you want me to send to")
        msg=takeCommand().lower()
        speak("Tell me the time when you want the messege to deliver")
        answer=takeCommand().lower()
        if "right now" in answer or "now" in answer:
            hours=int(datetime.datetime.now().hour)
            mins=int(datetime.datetime.now().minute)
            mins=mins+1
            pywhatkit.sendwhatmsg(contact_list[name],msg,hours,mins,20)
            speak("Messege sent")
        else:
            speak("Tell me the hour")
            hours=int(takeCommand())
            speak("Tell me the minutes")
            mins=int(takeCommand())
            pywhatkit.sendwhatmsg(contact_list[name],msg,hours,mins)
            speak("I will deliver the messege on time sir")
    else:
        speak("The name is not there in you contact list")
        speak("Please tell me the number")
        ph=takeCommand()
        phone="+91" + ph
        contact_list[name]=phone
        speak("Tell me the messege that you want to deliver")
        msg=takeCommand()
        speak("Tell me the time when you want the messege to deliver")
        answer = takeCommand()
        if "right now" in answer or "now" in answer:
            hours = int(datetime.datetime.now().hour)
            mins = int(datetime.datetime.now().minute)
            mins=mins+1
            pywhatkit.sendwhatmsg(contact_list[name],msg,hours,mins,20)
            speak("Messege sent")
        else:
            speak("Tell me the hour")
            hours = int(takeCommand())
            speak("Tell me the minutes")
            mins = int(takeCommand())
            pywhatkit.sendwhatmsg(contact_list[name], msg,hours,mins)
            speak("I will deliver the messege on time sir")

def screenshot():
    speak("In which name do you want to this screenshot?")
    name=takeCommand()
    file_name=name + ".png"
    path_name="D:\\Alpha Project\\Additionals\\Screenshots\\" + file_name
    kk=pyautogui.screenshot()
    kk.save(path_name)
    os.startfile("D:\\Alpha Project\\Additionals\\Screenshots")
    speak("Here is your screenshot")

