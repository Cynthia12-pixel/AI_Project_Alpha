import datetime
import time
import speech_recognition as sr
import pyttsx3
import webbrowser
import pywhatkit
import wikipedia
import os
import pyautogui
import keyboard
import pyjokes
from playsound import playsound
import requests
import bs4
import pytube
import googletrans
import smtplib
import email

contact_list={"maa":"+919735148140","baba":"+918389866655","suraj":"+918436924914","monalisa":"+918317849723","rohit":"+917278174562"}
email_list={"baba":"sourav.ghosal73@gmail.com","someone":"purisurajkumar@gmail.com","priyanka":"tuktuki.ghosal@gmail.com"}
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[1].id)

def speak(audio):                #speaking function
    print(f"-->>{audio}\n")
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        r.energy_threshold=350
        r.adjust_for_ambient_noise(source)
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
            results = wikipedia.summary(query, sentences=5)
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
    speak("Do you want me to suggest you the first video for your search?")
    answ=takeCommand().lower()
    if "yes" in answ:
        pywhatkit.playonyt(query)
        speak("Do you want me to play this video?")
        ans=takeCommand().lower()
        if "yes" in ans:
            youtube_auto('play')
        else:
            speak("ok")
    else:
        speak("ok")

def youtube_auto(query):
    if "fullscreen" in query:
        keyboard.press_and_release('f')
    elif "play" in query:
        keyboard.press_and_release('space bar')
    elif "pause" in query:
        keyboard.press_and_release('space bar')
    elif "restart" in query:
        keyboard.press_and_release('0')
    elif "mute" in query or "unmute" in query:
        keyboard.press_and_release('m')
    elif "skip" in query:
        keyboard.press_and_release('l')
    elif "back" in query:
        keyboard.press_and_release('j')
    elif "raise the volume" in query or "increase the volume" in query:
        keyboard.press_and_release('up arrow')
    elif "decrease the volume" in query:
        keyboard.press_and_release('down arrow')
    speak("Done")

def websiteSearch():
    speak("Tell the name of the website only")
    name = takeCommand().lower()
    if name != "none":
        speak("Launching the website")
        web1 = "https://www." + name + ".com"
        webbrowser.open(web1)
        speak("Done")

def openApps(query):
    if "vs code" in query or "visual studio code" in query:
        os.startfile('C:\\Users\\ASUS\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk')
    elif "chrome" in query:
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk")
    elif "notepad" in query:
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\Notepad.lnk")
    elif "py charm" in query or "pycharm" in query:
        os.startfile("C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains\\PyCharm Community Edition 2021.1.2.lnk")
    elif "microsoft edge" in query or "edge" in query:
        os.startfile("C:\\Users\\Public\\Desktop\\Microsoft Edge.lnk")
    speak ("Done")

def closeApps(query):
    if "vs code" in query or "visual studio code" in query:
        os.system("TASKKILL /F /im Code.exe")
    elif "chrome" in query:
        os.system("TASKKILL /F /im Chrome.exe")
    elif "notepad" in query:
        os.system("TASKKILL /F /im notepad.exe")
    elif "pycharm" in query or "py charm" in query:
        os.system("TASKKILL /F /im pycharm64.exe")
    elif "microsoft edge" in query or "edge" in query:
        os.system("TASKKILL /F /im msedge.exe")
    speak('The app is successfully closed')

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
    speak("To whom do you want to send the message?")
    name=takeCommand().lower()
    if name in contact_list.keys():
        msg=speak("Tell me the message that you want me to send to")
        msg=takeCommand().lower()
        speak("Tell me the time when you want the message to deliver")
        answer=takeCommand().lower()
        if "right now" in answer or "now" in answer:
            hours=int(datetime.datetime.now().hour)
            mins=int(datetime.datetime.now().minute)
            mins=mins+2
            pywhatkit.sendwhatmsg(contact_list[name],msg,hours,mins,32)
            pyautogui.click(1050, 950)
            time.sleep(2)
            keyboard.press_and_release("enter")
            speak("Message sent")
        else:
            speak("Tell me the hour")
            hours=int(takeCommand())
            speak("Tell me the minutes")
            mins=int(takeCommand())
            speak("I will deliver the message on time sir")
            pywhatkit.sendwhatmsg(contact_list[name],msg,hours,mins,32)
            pyautogui.click(1050,950)
            time.sleep(2)
            keyboard.press_and_release("enter")
            speak("Message Sent")
    else:
        speak("The name is not there in you contact list")
        speak("Please tell me the number")
        ph=takeCommand()
        phone="+91" + ph
        contact_list[name]=phone
        speak("Tell me the message that you want to deliver")
        msg=takeCommand()
        speak("Tell me the time when you want the message to deliver")
        answer = takeCommand()
        if "right now" in answer or "now" in answer:
            hours = int(datetime.datetime.now().hour)
            mins = int(datetime.datetime.now().minute)
            mins=mins+2
            pywhatkit.sendwhatmsg(contact_list[name],msg,hours,mins,32)
            pyautogui.click(1050, 950)
            time.sleep(2)
            keyboard.press_and_release("enter")
            speak("Message sent")
        else:
            speak("Tell me the hour")
            hours = int(takeCommand())
            speak("Tell me the minutes")
            mins = int(takeCommand())
            speak("I will deliver the message on time sir")
            pywhatkit.sendwhatmsg(contact_list[name], msg,hours,mins)
            pyautogui.click(1050, 950)
            time.sleep(2)
            keyboard.press_and_release("enter")
            speak("Message Sent")

def screenshot():
    speak("In which name do you want to this screenshot?")
    name=takeCommand()
    file_name=name + ".png"
    path_name="C:\\Users\\ASUS\\AI_Project_Alpha\\Additionals\\Screenshots\\" + file_name
    kk=pyautogui.screenshot()
    kk.save(path_name)
    os.startfile("C:\\Users\\ASUS\\AI_Project_Alpha\\Additionals\\Screenshots")
    speak("Here is your screenshot")

def jokes():
    joke=pyjokes.get_joke()
    speak(joke)

def alarm():
    speak("Tell the date in day month and year format")
    date=takeCommand()
    d_list=date.split(" ")
    ye=int(d_list[2])
    mon=int(d_list[1])
    da=int(d_list[0])
    speak("Tell the hour of the alarm")
    hr=int(takeCommand())
    speak("Tell the minutes of the alarm")
    min=int(takeCommand())
    alarm_time=datetime.datetime(ye,mon,da,hr,min)
    a_time=alarm_time.strftime("20%y-%m-%d %H:%M")
    while True:
        now = datetime.datetime.now()
        nowf = now.strftime("20%y-%m-%d %H:%M")
        if nowf==a_time:
            speak("Wake up")
            playsound("C:\\Users\\ASUS\\AI_Project_Alpha\\Alarmm.mp3",block=True)
        elif nowf>a_time:
            break

def videoDownloader():
    speak("Enter the URL of the video that you want to download")
    link=input("Enter the URL:")
    url=pytube.YouTube(link)
    video=url.streams.first()
    video.download("C:\\Users\\ASUS\\AI_Project_Alpha\\Additionals\\Youtube Videos")
    speak("Video downloaded")

def takeHindi():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='hi')
        print(f"You Said:-{query}\n")
        return query
    except:
        speak("Please Repeat")
        quer=takeCommand()
        return quer

def Tran():
    speak("Tell the sentence that you want to translate")
    line=takeHindi()
    translator = googletrans.Translator()
    translate_text = translator.translate(line,dest='en')
    speak(translate_text.text)

def remember(query):
    remember_msg=query
    remember_msg=remember_msg.replace("remember that","")
    remember_msg=remember_msg.replace("alpha","")
    speak("You are telling me to remind you that\n"+remember_msg)
    rememberr=open("data.txt","w")
    rememberr.write(remember_msg)
    rememberr.close()

def reminder():
    msg=open("data.txt","r")
    speak("You told me remind you that :"+msg.read())

def Temp(query):
    quer=query
    quer=quer.replace("alpha","")
    quer=quer.replace("what is the","")
    quer=quer.replace("tell me the","")
    quer=quer.replace("tell the","")
    quer=quer.replace("please","")
    quer=quer.replace("I want to know the","")
    quer=quer.replace("temperature of","temperature in")
    quer=quer.replace("temperature at","temperature in")
    print(quer)
    url="https://www.google.com/search?q=" + quer
    r=requests.get(url)
    data=bs4.BeautifulSoup(r.text,"html.parser")
    temper=data.find("div",class_="BNeawe")
    speak("The "+quer+" is " + temper.text)

def sendEmail():
    speak("To whom do you want to send the mail?")
    to=takeCommand().lower()
    if to in email_list.keys():
        content = email.message.EmailMessage()
        speak("What do you want to write in the mail?")
        msg=takeCommand().capitalize()
        content.set_content(msg)
        content.add_header("From", "priyankaghosal12122000@gmail.com")
        content.add_header("To", email_list[to])
        speak("Tell me the subject of the mail")
        sub = takeCommand().capitalize()
        content.add_header("Subject", sub)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login("priyankaghosal12122000@gmail.com", "Priyanka1212")
            server.send_message(content,"priyankaghosal12122000@gmail.com",email_list[to])
            server.close()
            speak("Message Sent")
        except:
            speak("There is some problem in sending the mail")
    else:
        speak("The name of the recipent is not there in your email_directory")
        speak("Please enter the email id of the recipent")
        to=input("Email ID of the recipent:")
        content=email.message.EmailMessage()
        speak("What do you want to write in the mail?")
        msg= takeCommand().capitalize()
        content.set_content(msg)
        content.add_header("From", "priyankaghosal12122000@gmail.com")
        content.add_header("To",to)
        speak("Tell me the subject of the mail")
        sub = takeCommand().capitalize()
        content.add_header("Subject", sub)
        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.ehlo()
            server.starttls()
            server.login("priyankaghosal12122000@gmail.com", "Priyanka1212")
            server.send_message(content,"priyankaghosal12122000@gmail.com",to)
            server.close()
            speak("Message sent")
        except:
            speak("There is some problem in sending the mail")
