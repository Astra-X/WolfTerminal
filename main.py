import imp
import os
import time
import getpass

import tld
import config
from playsound import PlaysoundException , playsound
from gtts import gTTS



# print("\033[1;32;40m")
os.system("clear")
t1 = gTTS(f'Welcome{config.username}' , lang = 'en' , tld = 'com.au')
t1.save("audio/welcome.mp3")

playsound("audio/welcome.mp3")
correctpass = (config.password)
loop ='true'
while loop == 'true':
    time.sleep(0.5)
    a = '''                                                                                            
                                                            .:                                              ..                         
                                                         .^!JY!                                            ^5J7^.                      
                                                      .:~G5. !B.                                           G?  ?B7:.                   
                                               .^!7?^.^ !5: :BJ                                            ?B^ .YJ ^^.~7!^.            
                                             .::JJ~7~7.:7  ^GB~Y7                                        ~J~PB~  !~ ~~!?!P7:.          
                                         .:!?^   :^ .J.:  7B5~:PP                                        5B~!PBJ  ~ ?!..^:  .!!:.      
                                    :~~^:^~JY :. 7  ^?   .7:  .?:                                        ^Y.  ^J^   !~  ~^ : .GY!^^^^:.
                                    YJ   ^~...?  P???.   .   :^                                           .^.   .    ??:J? :! . ^:  .JP
                                     ^^...5BJ^Y!^BB!   :: .!Y^                                              ^?~  :.   ^P#J 7J^?GY.  :!:
                                       ~7:^:. .5##?   7! .:~~                                                !?^: ^!.  :BBP5::~?7^!^.  
                                      ~BJ       7GY   J: . :.                                                 ^ :  Y^  .GB?.      J5.  
                                     ~BBB!        ~7. ^:   .                                                  :    !. .??:       ^B&P. 
                                    :J~:!G~         ~  .                                                          .: .~.        :G5?5Y.
                                    ^    ?Y         .                                                                ^          5J   ^!
                                         !7                                                                                     5^     
                                         !.                                                                                     ~!     
                                        ..                                                                                       ^     
                                                                                                    
 
    '''
    print(a)
    playsound('audio/pass.mp3')
    print("                                                                 ~~~~~~~~~~~[ENTER PASSWORD]>~~~~~~~~~~~")
    password = getpass.getpass("")
    os.system("clear")
    if password == correctpass:
        playsound("audio/gra.mp3")
        os.system("clear")
        loop ='false'
        loop1 = 'false'
    else:
        playsound("audio/de.mp3")
        print("password incorrect")
        
    
    

os.system(" python3 terminal.py")


