import os
import time
from gtts import gTTS
from playsound import playsound
import json
import config



# buddy = gTTS(f'hey {config.username}.i am your Artificial Intelligence. What you want to call me' , lang = 'en' , tld = 'com.au')
# buddy.save("audio/ai.mp3")
# playsound("audio/ai.mp3")

ai = input("What name you wanna give to your ai ~~~~> ")
username = input("What should I call you ~~~~> ")
password = input("set a  ~~~~> ")



# def dump_config(name: str, password):
#     with open("config.json", "w+") as f:
#         json.dump({"name": name, "password": password}, f)


# try:
#     with open("config.json", "r") as f:
#         data = json.load(f)
#         if data == {}:
#             name = input("<Enter what you want to set input> ")
#             password = input("Enter what you want to set password:")
#             dump_config(name, password)
#             login()
#         else:
#             login()
# except Exception as e:
#     print(e)


t1 = gTTS(f"my name is {ai}, now we are gonna setup your advanced hacking terminal with above 100 self developed tools" , lang = 'en' , tld = 'com.au')
# t1.save("audio/welcome.mp3")
print(t1)
# playsound("audio/welcome.mp3")
a = '''         

   WITH GREAT POWERS 
COME GREAT RESPONSIBILITY

_____________________________________________
|||||||Which operating system you have|||||||
_____________________________________________

=[1]  kali
=[2]  parrot
=[3]  termux
'''
print(a)

op = input("~~~~~~>")
if op == '1':
   os.system("sudo apt install pkg-config")    
   os.system("sudo apt-get install libcairo2-dev")        
   os.system("sudo apt-get install libgirepository1.0-dev")                
   time.sleep(3)
   os.system("pip3 install -r requirements.txt")
   


