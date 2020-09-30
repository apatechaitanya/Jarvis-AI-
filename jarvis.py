import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
from pyttsx3 import engine
from email.mime import audio
from pyttsx3.drivers import sapi5
from comtypes.gen import SpeechLib

print("Initializing Jarvis")



engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)
engine.say(" Hi Chaitanya")
engine.runAndWait()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    
    speak("I am Jarvis memory one tera byte Please tell me how can i help you")
  

def takeCommand():
    #it takes the input from user by microphone and it will text it
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio =r.listen(source)
    try:
        print("Recognizing...")
        query =r.recognize_google(audio)
        print(f"User said : {query}\n")
    except Exception as e:
        print(e)

        print("Say that again please.... ")
        return "None"
    return query
    


    
        

if __name__ =="__main__":
    wishMe()
    s = {"How are you","jarvis"}
    while  True:
       query = takeCommand().lower()
       #logic to executing task based on query
       if 'wikipedia' in query:
           speak("searching wikipedia....")
           query = query.replace("wikipedia", "")
           results = wikipedia.summary(query,sentences=2)
           print("According to wikipedia.....")
           speak("According to wikipedia")
           print(results)
           speak(results)
       elif 'open youtube' in query:
            webbrowser.open("youtube.com")
       elif 'open google' in query:
            webbrowser.open("google.com")
       elif 'open gmail' in query:
            webbrowser.open("gmail.com")
       elif 'open stack overflow' in query:
            webbrowser.open("stackoverflow.com")
       elif 'open github' in query:
            webbrowser.open("github.com")
       elif 'open code' in query:
            code = "C:\\Users\\reliance\\AppData\\Local\\Programs\\Code.exe"
            os.startfile(os.path.join(code)) 
       elif 'play music' in query:
            music_dir = 'D:\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))
       elif 'time' in query:
           strTime = datetime.datetime.now().strftime("%H:%M:%S")
           print(f"Time is :{strTime}")
           speak(f"Time is :{strTime}")
       elif 'vlc' in query:
            vlc= "C:\\Users\\reliance\\Downloads"
            os.startfile(os.path.join(vlc))
           
       elif 'atom' in query:
            atom= "C:\\Users\\reliance\\Downloads\\AtomSetup-x64.exe"
            os.startfile(os.path.join(atom))
       
       elif 'how are you' in query:
          speak("i am fine you have good day")
        
    


