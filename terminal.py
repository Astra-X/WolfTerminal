from calendar import SATURDAY
from http import client
import os
from datetime import datetime
from playsound import playsound
from gtts import gTTS
import config
import time
from unicodedata import name
now = datetime.now()
current_time = now.strftime('%H:%M:%S')


def help():

    help1 = '''\033[1;32;40m
    _________________________________________________________________
    THIS TOOL IS CREATED FOR THOSE WHO REALLY WANT TO LEARN SOMETHING 
    
                        CREATED BY WOLVES
        
        \033[1;33;40mstudy\033[1;32;40m  -    can give you content related to CyberSec
        \033[1;33;40mtool\033[1;32;40m   -    all tools used in CyberSec



            
        

    
    

    
    
    
    
    
    
    
    '''
    print(help1)
def sta():
    sta1 = '''\033[1;31;40m
                                        -----------  ATTRIBUTES  -----------\033[1;34;40m



                             ::\033[1;32;40mnetwork                             : STUDY NETWORKING

                             \033[1;34;40m::\033[1;32;40mnmap                                : STUDY ENUMERATION
            

    
    
    
    
    
    
    
    '''
    print(sta1)
def network1():
    networking = '''\033[1;34;40m
                              COMPLETE TASK TO GO TO ANOTHER PAGE
                            TRY TO UNDERSTAND THE BASICS OF NETWORKING

         ###########################||\033[1;33;40mWHAT IS NETWORKING\033[1;34;40m||###########################\033[1;32;40m
    
            Computer Network is a group of computers connected with each other through wires, 
            optical fibres or optical links so that various devices can interact with each other through a network.

            The aim of the computer network is the sharing of resources among various devices.
            In the case of computer network technology, there are several types of networks that vary from simple to complex level.


 ###########################||\033[1;33;40mComponents of Computer Network\033[1;32;40m||###########################\033[1;32;40m
    
                _____  \033[1;31;40mMajor components of a computer network are:\033[1;32;40m  _____

    \033[1;31;40mNIC(National interface card):\033[1;32;40m

            NIC is a device that helps the computer to communicate with another device. 
            The network interface card contains the hardware addresses, the data-link layer protocol use this address to 
            identify the system on the network so that it transfers the data to the correct destination.

                _____  \033[1;31;40mThere are two types of NIC:\033[1;32;40m _____
                
        
        \033[1;34;40mWireless NIC:\033[1;32;40m

                    All the modern laptops use the wireless NIC. In Wireless NIC, a connection is made using the antenna that employs the radio wave technology.

        \033[1;34;40mWired NIC:\033[1;32;40m

                    Cables use the wired NIC to transfer the data over the medium.
                    


    \033[1;31;40mHub\033[1;32;40m

            Hub is a central device that splits the network connection into multiple devices.
            When computer requests for information from a computer, it sends the request to the Hub.
            Hub distributes this request to all the interconnected computers.



    \033[1;31;40mSwitches\033[1;32;40m

            Switch is a networking device that groups all the devices over the network to transfer the data to another device.
            A switch is better than Hub as it does not broadcast the message over the network, i.e., it sends the message to the device for which it belongs to.
            Therefore, we can say that switch sends the message directly from source to the destination.



    \033[1;31;40mCables and connectors:\033[1;32;40m

            Cable is a transmission media that transmits the communication signals.

              _____  \033[1;31;40mThere are three types of cables:\033[1;32;40m  _____

        \033[1;34;40mTwisted pair cable:\033[1;32;40m
                    It is a high-speed cable that transmits the data over 1Gbps or more.

        \033[1;34;40mCoaxial cable:\033[1;32;40m
                    Coaxial cable resembles like a TV installation cable.
                    Coaxial cable is more expensive than twisted pair cable, but it provides the high data transmission speed.

        \033[1;34;40mFibre optic cable:\033[1;32;40m
                    Fibre optic cable is a high-speed cable that transmits the data using light beams.
                    It provides high data transmission speed as compared to other cables.
                    It is more expensive as compared to other cables, so it is installed at the government level.



    \033[1;31;40mRouter:\033[1;32;40m

            Router is a device that connects the LAN to the internet.
            The router is mainly used to connect the distinct networks or connect the internet to multiple computers.

    \033[1;31;40mModem:\033[1;32;40m

            Modem connects the computer to the internet over the existing telephone line.
            A modem is not integrated with the computer motherboard. A modem is a separate part on the PC slot found on the motherboard.

 ###########################||\033[1;33;40mUses Of Computer Network\033[1;32;40m||###########################

    \033[1;31;40mResource sharing:\033[1;32;40m
            Resource sharing is the sharing of resources such as programs, printers, and data among the users on
            the network without the requirement of the physical location of the resource and user.



    \033[1;31;40mServer-Client model:\033[1;32;40m
            Computer networking is used in the server-client model.
            A server is a central computer used to store the information and maintained by the system administrator.
            Clients are the machines used to access the information stored in the server remotely.



    \033[1;31;40mCommunication medium:\033[1;32;40m
            Computer network behaves as a communication medium among the users.
            For example, a company contains more than one computer has an email system which the employees use for daily communication.



    \033[1;31;40mE-commerce:\033[1;32;40m
            Computer network is also important in businesses.
            We can do the business over the internet.
            For example, amazon.com is doing their business over the internet, i.e., they are doing their business over the internet.
    
    '''
    print(networking)
def network2():

    networking2 = '''\033[1;32;40m
    
###########################||\033[1;33;40mFeatures Of Computer Network\033[1;32;40m||###########################
                             _________________________________________________________            

                             _____  \033[1;31;40mLIST OF FEATURES:\033[1;32;40m  _____


                                    THERE ARE 7 FEATURES OF COMPUTER NETWORK

    \033[1;31;40mCommunication speed:\033[1;32;40m

            Network provides us to communicate over the network in a fast and efficient manner.
             For example, we can do video conferencing, email messaging, etc. over the internet.
              Therefore, the computer network is a great way to share our knowledge and ideas.
    
    
    \033[1;31;40mFile sharing:\033[1;32;40m

            File sharing is one of the major advantage of the computer network.
             Computer network provides us to share the files with each other.


    \033[1;31;40mBack-up and Roll Back is easy:\033[1;32;40m 

            Since the files are stored in the main server which is centrally located.
             Therefore, it is easy to take the back up from the main server.

    
    \033[1;31;40mSoftware and Hardware sharing:\033[1;32;40m

            We can install the applications on the main server, therefore, the user can access the applications centrally.
             So, we do not need to install the software on every machine. Similarly, hardware can also be shared.


    \033[1;31;40mSecurity:\033[1;32;40m

            Network allows the security by ensuring that the user has the right to access the certain files and applications.


    \033[1;31;40mScalability:\033[1;32;40m

            Scalability means that we can add the new components on the network.
             Network must be scalable so that we can extend the network by adding new devices.
              But, it decreases the speed of the connection and data of the transmission speed also decreases, this increases the chances of error occurring. 
               This problem can be overcome by using the routing or switching devices.

        
     \033[1;31;40mReliability:\033[1;32;40m

            Computer network can use the alternative source for the data communication in case of any hardware failure.
    '''
    
    print(networking2)
def osi():
    osi1 = ''' \033[1;32;40m

    
    
    
    
    
    
    
    '''
    

 
os.system("clear")
playsound('audio/wolves.mp3')

b = '''\033[1;35;40m 
                                            ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\033[1;31;40m
                                                \033[1;31;40m
                                                                _____________________________________________
                                                                |                                           |
                                                                |               WE ARE WOLVES               |
                                                                |   WE ARE TRYING TO UPGRADE SCRIPT KIDDIES |
                                                                ▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔▔ \033[1;32;40m
                                                            .:                                              ..
                                                         .^!JY!                                            ^5J7^.
                                                      .:~G5. !B.                                           G?  ?B7:.
                                               .^!7?^.^ !5: :BJ                                            ?B^ .YJ ^^.~7!^.
                                             .::JJ~7~7.:7  ^GB~Y7                                        ~J~PB~  !~ ~~!?!P7:.
                                         .:!?^   :^ .J.:  7B5~:PP                                        5B~!PBJ  ~ ?!..^:  .!!:.
                                    :~~^:^~JY :. 7  ^?   .7:  .?:  \033[1;30;40m ^^  .^:  .^:  .^~^.   :^.    ^^^^:\033[1;32;40m   ^Y.  ^J^   !~  ~^ : .GY!^^^^:.
                                    YJ   ^~...?  P???.   .   :^     \033[1;31;40mP@7 J@@^ G@7.5&BPB&P..#@!    ^@@PPJ\033[1;32;40m    .^.   .    ??:J? :! . ^:  .J
                                     ^^...5BJ^Y!^BB!   :: .!Y^      \033[1;31;40m~@B:&B&5~@B J@#   #@J #@!    ^@@5Y!\033[1;32;40m      ^?~  :.   ^P#J 7J^?GY.  :!:
                                       ~7:^:. .5##?   7! .:~~        \033[1;31;40m5@B@~Y@B@! !@@!:!@@7 &@?^^. ^@@?!^\033[1;32;40m      !?^: ^!.  :BBP5::~?7^!^.
                                      ~BJ       7GY   J: . :.        \033[1;31;40m^PGY :PGY   ~5GGG5~ .5GPPP! :PP.\033[1;32;40m          ^ :  Y^  .GB?.      J5.
                                     ~BBB!        ~7. ^:   .                                                  :    !. .??:       ^B&P.
                                    :J~:!G~         ~  .                                                          .: .~.        :G5?5Y.
                                    ^    ?Y         .                                                                ^          5J   ^!
                                         !7                                                                                     5^
                                         !.                                                                                     ~!
                                        ..                                                                                       ^
                                                                    \033[1;31;40m <<<<<<<<<<<<||\033[1;33;40mSUPPORT US\033[1;31;40m||>>>>>>>>>>>>\033[1;34;40m
                                                                    <<<<||\033[1;31;40m DONATE          CRYPTO \033[1;34;40m||>>>>\033[1;31;40m
                                                        <<<<<<<<\033[1;32;40mbc1quh3wq38ajp23qyjca8vxhj72pcea43frg63e0f\033[1;31;40m>>>>>>>>

                                                                \033[1;34;40m############\033[1;31;40mTYPE \033[1;32;40mHELP\033[1;31;40m FOR COMMANDS\033[1;34;40m############


\033[1;31;40m'''
print(b)
loop ='true'
while loop == 'true':
    print(f"\033[1;32;40m┌────────[\033[1;31;40m{config.username}\033[1;32;40m]────────[\033[1;30;40m{current_time}\033[1;32;40m]")
    command = input("\033[1;32;40m└─~~>\033[1;33;40m")
    print('\033[1;35;40m')
    if command=='help':
        help()

    elif command == 'study':
        print(" CHOOSE ATTRIBUTE TO STUDY ON")
        sta()
    elif command == 'wolf':
        os.system("python3 Wolf.py")

    elif command == 'study' + ' ' + 'network':
        print("\033[1;33;40mIf you dont remember the page try '\033[1;31;40mnetwork pages\033[1;33;40m'")
        page = input("======|ENTER THE PAGE YOU WANT TO STUDY ON|======")
        if page == '1':
            network1()
            pagenet = input('≡≡≡≡≡≡≡|WANT TO GO TO SECOND PAGE|≡≡≡≡≡≡≡⫸ ')
            if pagenet == 'yes':
                os.system("clear")
                print("             \033[1;34;40mTO GOTO PAGE 2 YOU NEED TO COMPLETE THESE TASKS\033[1;31;40m")
                test1 = input(" Q1_ \033[1;32;40m ____________\033[1;31;40m is a central device that splits the network connection into multiple devices.")
                test2 = input(" Q2_ \033[1;32;40m ____________\033[1;31;40m are the machines used to access the information stored in the server remotely.")
                if test1 != 'hub':
                    print("wrong!")
                if test2 != 'clients':
                    print("wrong!")

                if test1 + test2 == 'hub' 'clients':
                    t1 = gTTS(f'congrats {config.username} for completing task. do researching on next page' , lang = 'en' , tld = 'com.au')
                    t1.save("audio/task.mp3")
                    playsound("audio/task.mp3")
                    os.system("clear")
                    network2()
                else:
                    print("\033[1;31;40mTRY TO RESEARCH MORE ON THIS TOPIC")
                    time.sleep(3)
                    os.system("clear")
                    print()
        if page == '2':
            network2()
            pagenet1 = input('≡≡≡≡≡≡≡|WANT TO GO TO THIRD PAGE|≡≡≡≡≡≡≡⫸ ')
            if pagenet1 == 'yes':
                os.system("clear")
                print("             \033[1;34;40mTO GOTO PAGE 3 YOU NEED TO COMPLETE THESE TASKS\033[1;31;40m")
                test3 = input(" Q1_ \033[1;32;40m ____________\033[1;31;40m is a central device that splits the network connection into multiple devices.")
                test4 = input(" Q2_ \033[1;32;40m ____________\033[1;31;40m are the machines used to access the information stored in the server remotely.")
                
        
 
    elif command == 'time':
        print("Current Time is:--"  , current_time)

    elif command == 'sudo':
        os.system('')
    
    elif command== 'exit':
        loop = 'false'
        print("\033[1;32;40mWolf\033[1;31;40m Is\033[1;33;40m Waiting\033[1;34;40m For\033[1;35;40m You \033[1;31;40mTo \033[1;32;40mCome Back ")
        
        exit()
    elif command == command:
        os.system(command)        
            


    elif command == 'exit':
        loop == 'false'
        exit
    else:
        print(f'[{command}] is not found, try help!')





    
