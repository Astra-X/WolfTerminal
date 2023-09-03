import pyttsx3
# from decouple import config
import pyautogui 
import pywhatkit as kit
import os
import datetime
import speech_recognition as sr
from random import choice
import youtube_dl
# import chatterbot
import wikipedia
import webbrowser
import time
import spotdl
# from utils import opening_text

USERNAME = "saaz"
BOTNAME = "Lucy"

keywords = ["search","on google","on youtube"]

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

def download_song(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

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
            

        if 'wait a second' in query:
            time.sleep(5)
            
            
        if 'notepad' in query:
            os.system("start apps\\notepad")
        
        
        if 'brave'in query:
            os.system("start apps\\brave")
                
                
        if 'download' in query:
            if 'from youtube' in query:
                # query = query.replace(["download","from youtube"],"")
                song_url = "https://www.youtube.com/watch?v=0XyV-vw5II4"
                download_song(song_url)
                
                
        if 'play' in query:
            if 'youtube' in query:
                query = query.replace("on youtube","")
                kit.playonyt(query)
            
            
        if 'whatsapp' in query:
            speak("whom you want to send message")
            whatsapp_number = take_user_input()
            speak("what's the message")
            whatsapp_msg = take_user_input()
            kit.sendwhatmsg_instantly("+91" + whatsapp_number,whatsapp_msg)
            pyautogui.press("enter")
        if 'search' in query:    
            if 'on google' in query:
                query1 = query.replace(sy,"")
                

                kit.search(query1)
        if 'what is' in query:
            query1 = query.replace("what is","")
            
            speak(kit.info((query1), lines = 1))
            
            
        if 'calculator' in query:
            if 'add' or '+' in query:
                
                speak("what's the first number")
                
            # print("\nSuccessfully Searched")
        
