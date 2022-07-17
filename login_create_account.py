from role_sorter import *
import pytz
import pandas as pd
import smtplib
import numpy as np      
import sqlite3
from datetime import datetime
import random


def main():
    choice=input("enter 1 to make a new account and enter 2 to login to yur account and 3 to exit ") #gives uer option top start program all over or end it 
    if choice=="1":
        create()
    if choice =="2":
        login() 
    if choice == "3":
        exit() 

def  login():
    print("""type 1  to  get option for exit porgram or  to go to main menu""")
    print("""type 2  to login to your account""")

    choice=input(":")
    if choice=="1":
        exit() 

    elif choice == "2":
        print("""type 1 anytime  to  get option for exit porgram or  to go to main menu""")
        conect=sqlite3.connect("C:/Users/Talha/Desktop/work/wolf-terminal/db/system_roles.db")
        c=conect.cursor()
        r=c.execute("""SELECT username FROM unbanned_user""").fetchall()
        list_username=tuple(i[0] for i in r)

        login_username=input("Enter username:")
        if login_username in list_username:
            password=c.execute("SELECT PWD FROM unbanned_user WHERE username=?", (login_username,)).fetchall()
            password=tuple(i[0] for i in password)

            login_password=input("Enter password:")
            if login_password==password[0]:
                role=c.execute("SELECT roles FROM unbanned_user WHERE username=?", (login_username,)).fetchall()
                list_roles=tuple(i[0] for i in role)


                if "ethical_admin"==list_roles[0]:
                    tz=pytz.timezone("Europe/London")
                    time=datetime.now(tz)
                    time=str(time)
                    f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a")
                    f.write(login_username + " admin_ethical "+time+"\n")
                    f.close()
                    from_role="admin_ethicals"
                    admin_ethicals(login_username,login_password,from_role)

                elif "dev_admin"==role[0]:
                    tz=pytz.timezone("Europe/London")
                    time=datetime.now(tz)
                    time=str(time)
                    f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a")
                    f.write(login_username + " dev_admin "+time+"\n")
                    f.close()
                    from_role="admin_dev"
                    admin_dev(login_username,login_password,from_role )

                elif "dev" == role[0]:
                    tz=pytz.timezone("Europe/London")
                    time=datetime.now(tz)
                    time=str(time)
                    f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a")
                    f.write(login_username + " dev "+time+"\n")
                    f.close()
                    from_role="dev"
                    dev(login_username,login_password,from_role)

                elif "mod" == role[0]:
                    tz=pytz.timezone("Europe/London")
                    time=datetime.now(tz)
                    time=str(time)
                    f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a")
                    f.write(login_username + " mod "+time+"\n")
                    f.close()
                    from_role="mod"
                    mod(login_username,login_password,from_role)

                elif "helpers" ==role[0]:
                    tz=pytz.timezone("Europe/London")
                    time=datetime.now(tz)
                    time=str(time)
                    f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a")
                    f.write(login_username + " helper "+time+"\n")
                    f.close()
                    from_role="helper"
                    helpers(login_username,login_password ,from_role)

                elif "member" == role[0]:
                    tz=pytz.timezone("Europe/London")
                    time=datetime.now(tz)
                    time=str(time)
                    f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a")
                    f.write(login_username + " member "+time+"\n")
                    f.close()
                    from_role="member"
                    member(login_username,login_password ,from_role)

                elif login_password=="1":
                    exit()

                else:
                    login()

        elif login_username  not in list_username:
            print("no account found")
            print("proceed to create a account")
            create()

        elif login_username=="1":
            exit()
    
    else:
        login()

def create():
    print("""type exit  to  get option for exit porgram or  to go to main menu""")
    print("""type 2  to create  to your account""")


    choice=input(":").lower()
    if choice=="exit":
        exit()
    
    elif choice == "2":


        conect=sqlite3.connect("C:/Users/Talha/Desktop/work/wolf-terminal/db/system_roles.db")
        c=conect.cursor()

        email_bolean=False
        while email_bolean == False:

            data_email = c.execute("""SELECT email FROM ubanned_user""").fetchall()
            email_list=tuple(i[0] for i in data_email) 
            email=input("enter email:").lower()
            if email =="exit":
                email_bolean=True
                exit()

            elif email in email_list:
                print("account already exist\n proceed to login")
                ch=input("enter 1 to to go ").lower()
                if ch == "1":
                    email_bolean=False

                elif ch == "2":
                    email_bolean=True
                    exit()

            elif  email  not in email_list and email is not "exit":
                ch=input("enter 1 to create account with diffrent email and  2 for exit and main  menu ").lower()

                if ch == "1":
                    email_bolean=False

                elif ch == "2":
                    email_bolean=True
                    exit()
                else:
            else:
                print("error")
                ch=input("enter 1 to try  creating account and  2 for exit and main  menu ")

                if ch == "1":
                    email_bolean=False

                elif ch == "2":
                    email_bolean=True
                    exit()
        



def exit():

    print("do u wnat to go to main menu enter 1")
    print("do u want to exit the program enter 2")

    choice=input(":")
    if choice== "1":
        main()

    elif choice =="2":
        print("thanks for using our program ")

    else:
        exit()

main()