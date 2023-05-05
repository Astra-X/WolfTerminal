import pyttsx3
# from decouple import config
import os
import datetime
import speech_recognition as sr
from random import choice
import wikipedia
import webbrowser
import time
# from utils import opening_text

USERNAME = os.getlogin()
BOTNAME = "Astra"

engine = pyttsx3.init('sapi5')


#Set Rate
engine.setProperty('rate',190)

#set volume
engine.setProperty('volume', 1.0)

#Set voice

voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



opening_text = [
    "Cool, I'm on it sir.",
    "Okay sir, I'm working on it.",
    "Just a second sir.",
]


def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def greet_user():
    hour = 6
    if (hour >= 6) and (hour < 12):
        speak(f"Good Morning {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Good afternoon {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good Evening {USERNAME}")
    speak(f"I am {BOTNAME}. How may I assist you?")
    
def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("hmm....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
            
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query

def open(app):
    pass

def findfile(name, path):
    for dirpath, dirname, filename in os.walk("C:/Windows/"):
        if name in filename:
            return os.path.join(dirpath, name)
        
    


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()
        print(query)
        # if "open" in query:
        #     filepath = findfile((query), "/")
        #     print(filepath)
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Wait A Second buddy. Lemme have a look')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
         
        if 'stop buddy' in query:
            speak('Hope you liked me. I Think we can do many projects together. Have a nice day.')
            exit()
            
        if 'search' in query:
            query = query.replace("open", "")
            # open_ = webbrowser.open(query)
            if 'on youtube' in query:
                query = query.replace("on youtube", "")
                open_ = webbrowser.open("https://www.youtube.com/results?search_query=" + query)
                
                
                
                
            
        if 'wait a second' in query:
            time.sleep(5)
            
        if 'locate' in query:
            locate = query.replace('locate', "")
            filepath = findfile(locate, "/")
            print(filepath)
            
            
        # if 'open notepad' in query:
        #     query = query.replace("open", "")
        #     os.system("C:\Windows\\notepad.exe")
            
            
    