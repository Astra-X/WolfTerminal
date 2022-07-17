from secrets import choice
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from time import process_time
from login_create_account import *
import pytz
import os
import sqlite3

def admin_ethical(login_username,login_password):
    tz=pytz.timezone("Europe/London")
    time=datetime.now(tz)
    time=str(time)
    f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a")
    f.write(login_username + " "+time+"\n")
    f.close()
    
    role="admin_ethical"
    n="logged"
    choice=input("enter 1 to change roles, enter 2 to ban/delete user info , 3 for going to main menu or exit program:")
    if choice == "1":
        change_roles(login_username,login_password,role,n)
    elif  choice == "2":
        ban_delete_user_info(login_username,login_password,role,n)
    elif choice == "3":
        exit()
    else:
        role_sorter(role,n)

def admin_dev(login_username,login_password):
    tz=pytz.timezone("Europe/London")
    time=datetime.now(tz)
    time=str(time)
    f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a")
    f.write(login_username + " "+time+"\n")
    f.close()

    role="admin_dev"
    n="logged"
    choice=input("enter 1 to change roles, enter 2 to ban/delete user info , 3 for edit code and data base , 4 for going to main menu or exit program:")
    if choice == "1":
        change_roles(login_username,login_password,role,n)
    elif  choice == "2":
        ban_delete_user_info(login_username,login_password,role,n)
    elif choice == "3":
        edit_code_databse(login_username,login_password,role,n)
    elif choice == "4":
        exit()
    else:
        role_sorter(role,n)

def dev(login_username,login_password):
    tz=pytz.timezone("Europe/London")
    time=datetime.now(tz)
    time=str(time)
    f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a")
    f.write(login_username + " "+time+"\n")
    f.close()

    role="admin_dev"
    n="logged"

    choice=input("enter 1 to edit code and data base, enter 2 for going to main menu or exit program:")
    if choice == "1":
        edit_code_databse(login_username,login_password,role,n)
    elif choice == "2":
        exit()
    else:
        role_sorter(role,n)

def mod(login_username,login_password):
    tz=pytz.timezone("Europe/London")
    time=datetime.now(tz)
    time=str(time)
    f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a")
    f.write(login_username + " "+time+"\n")
    f.close()
    choice=input("enter 1 to ban/delete user info  , enter 2 for going to main menu or exit program:")

    role="mod"
    n="logged"
    if choice == "1":
        ban_delete_user_info(login_username,login_password,role,n)
    elif choice == "2":
        exit()
    else:
        role_sorter(role,n)

def helpers(login_username,login_password):
    tz=pytz.timezone("Europe/London")
    time=datetime.now(tz)
    time=str(time)
    f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a")
    f.write(login_username + " "+time+"\n")
    f.close()
    choice=input("enter 1 to reprt bug , enter 2 for going to main menu or exit program:")

    role="helpers"
    n="logged"

    if choice == "1":
        reportbug(login_username,login_password,role,n)
    elif choice == "2":
        exit()
    else:
        role_sorter(role,n)

def member(login_username,login_password):
    tz=pytz.timezone("Europe/London")
    time=datetime.now(tz)
    time=str(time)
    f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a")
    f.write(login_username + " "+time+"\n")
    f.close()

    role="member"
    n="logged"

    f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a")
    f.write(login_username + " "+time+"\n")
    f.close()



def change_roles(login_username,login_password,role,n):
    username=input("Enter usernameof svount u want  to change role of:")
    email=input("enter email:")
    conect=sqlite3.connect("system_roles.db")
    c=conect.cursor()
    user_username=c.execute("SELECT username FROM userdata WHERE email =?",(email,)).fetchall()
    user_username=tuple(i[0] for i in user_username)

    if username in user_username:
        role_update=input("do u want to update role to ethical admin enter 1, for  dev admin type 2 , for dev admin type 3, for  mod admin type 4 , for helper admin type 5 ,type 6 for member, type 7 for main and  for exit:")

        if role_update=="1":
            c.execute("""UPDATE userdata SET roles = "ethical_admin"  WHERE username=?""",(username,))
            f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a")
            f.write(login_username+"change role of"+username+"to ethical_admin"+"\r\n")
            f.close()
            conect.commit()
            conect.close()


            ch=input("enter 1 if u want to see otehr things u can do  and enter 2  if u want to see exit option or option to go to main menu")
            if ch == "1":
                print("here")
            elif ch=="2":
                main()
            else:
                print ("Sorry error plz try again")
                exit()
            
        elif role_update=="2":
            c.execute("""UPDATE userdata SET roles = "dev_admin"  WHERE username=?""",(username,))
            f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a")
            f.write(login_username+"change role of"+username+"to dev_admin"+"\r\n")
            f.close()
            conect.commit()
            conect.close()


            ch=input("enter 1 if u want to see otehr things u can do  and enter 2  if u want to see exit option or option to go to main menu")
            if ch == "1":
                print("here")
            elif ch=="2":
                main()
            else:
                print ("Sorry error plz try again")
                exit()

        elif role_update=="3":
            c.execute("""UPDATE userdata SET roles = "dev"  WHERE username=?""",(username,))
            f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a")
            f.write(login_username+"change role of"+username+"to dev"+"\r\n")
            f.close()
            conect.commit()
            conect.close()


            ch=input("enter 1 if u want to see otehr things u can do  and enter 2  if u want to see exit option or option to go to main menu")
            if ch == "1":
                print("here")
            elif ch=="2":
                main()
            else:
                print ("Sorry error plz try again")
                exit()

        elif role_update=="4":
            c.execute("""UPDATE userdata SET roles = "mod"  WHERE username=?""",(username,))
            f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a")
            f.write(login_username+"change role of"+username+"to mod"+"\r\n")
            f.close()
            conect.commit()
            conect.close()


            ch=input("enter 1 if u want to see otehr things u can do  and enter 2  if u want to see exit option or option to go to main menu")
            if ch == "1":
                print("here")
            elif ch=="2":
                main()
            else:
                print ("Sorry error plz try again")
                exit()

        elif role_update=="5":
            c.execute("""UPDATE userdata SET roles = "helpers"  WHERE username=?""",(username,))
            f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a")
            f.write(login_username+"change role of"+username+"to helper"+"\r\n")
            f.close()
            conect.commit()
            conect.close()


            ch=input("enter 1 if u want to see otehr things u can do  and enter 2  if u want to see exit option or option to go to main menu")
            if ch == "1":
                print("here")
            elif ch=="2":
                main()
            else:
                print ("Sorry error plz try again")
                exit()

        elif role_update=="6":
            c.execute("""UPDATE userdata SET roles = "member"  WHERE username=?""",(username,))
            f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a")
            f.write(login_username+"change role of"+username+"to member"+"\r\n")
            f.close()
            conect.commit()
            conect.close()

            ch=input("enter 1 if u want to see otehr things u can do  and enter 2  if u want to see exit option or option to go to main menu")
            if ch == "1":
                print("here")
            elif ch=="2":
                main()
            else:
                print ("Sorry error plz try again")
                exit()
        elif role_update=="7":
            exit()
    else:
        print ("Sorry error plz try again")
        exit()

def ban_delete_user_info(login_username,login_password,role,n):
    print("hi")

def edit_code_databse(login_username,login_password,role,n):
    choice=input("Please enter 1 to if u are editing database or 2 if u are editing code or 3 for main menu  or  to  exit:")
    if choice=="1":
        tz=pytz.timezone("Europe/London")
        time=datetime.now(tz)
        time=str(time)
        f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/edit_code.txt","a")
        f.write(login_username + " "+time+"\r\n")
        f.close
        exit()
    elif choice=="2":
        tz=pytz.timezone("Europe/London")
        time=datetime.now(tz)
        time=str(time)
        f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/edit_database.txt","a")
        f.write(login_username + " "+time +"\r\n")
        f.close
        exit()
    elif choice == "3":
        ch=input("enter 1 if u want to see otehr things u can do  and enter 2  if u want to see exit option or option to go to main menu")
        if ch == "1":
            print("here")
        elif ch=="2":
            main()
        else:
            print ("Sorry error plz try again")
            exit()
    else:
        exit()

def reportbug(login_username,login_password,role,n):
    tz=pytz.timezone("Europe/London")
    time=datetime.now(tz)
    time=str(time)
    f=open("C:/Users/Talha/Desktop/work/wolf-terminal/sqllitesutdio work/New folder/logfile/bug_report.txt","w+")
    f.write(login_username + " "+time +"\r\n")
    f.close
    
def unban(login_username,login_password,role,n):
    print("hi")



def admin_ethical_1(login_username,login_password):
    choice=input("enter 1 to change roles, enter 2 to ban/delete user info , 3 for going to main menu or exit program:")
    if choice == "1":
        change_roles(login_username,login_password)
    elif  choice == "2":
        ban_delete_user_info(login_username,login_password)
    elif choice == "3":
        exit()
    else:
        admin_ethical(login_username,login_password)

def admin_dev_1(login_username,login_password):
    choice=input("enter 1 to change roles, enter 2 to ban/delete user info , 3 for edit code and data base , 4 for going to main menu or exit program:")
    if choice == "1":
        change_roles(login_username,login_password)
    elif  choice == "2":
        ban_delete_user_info(login_username,login_password)
    elif choice == "3":
        edit_code_databse(login_username,login_password)
    elif choice == "4":
        exit()
    else:
        admin_dev(login_username,login_password)

def dev_1(login_username,login_password):
    choice=input("enter 1 to edit code and data base, enter 2 for going to main menu or exit program:")
    if choice == "1":
        edit_code_databse(login_username,login_password)
    elif choice == "2":
        exit()
    else:
        dev(login_username,login_password)

def mod_1(login_username,login_password):
    choice=input("enter 1 to ban/delete user info  , enter 2 for going to main menu or exit program:")
    if choice == "1":
        ban_delete_user_info(login_username,login_password)
    elif choice == "2":
        exit()
    else:
        mod(login_username,login_password)

def helpers_1(login_username,login_password):
    choice=input("enter 1 to reprt bug , enter 2 for going to main menu or exit program:")
    if choice == "1":
        reportbug(login_username,login_password)
    elif choice == "2":
        exit()
    else:
        helpers(login_username,login_password)

def member_1(login_username,login_password):
    print("hi")


def change_roles_1(login_username,login_password):

    username=input("Enter usernameof svount u want  to change role of:")
    email=input("enter email:")
    conect=sqlite3.connect("system_roles.db")
    c=conect.cursor()
    user_username=c.execute("SELECT username FROM userdata WHERE email =?",(email,)).fetchall()
    user_username=tuple(i[0] for i in user_username)

    if username in user_username:
        role_update=input("do u want to update role to ethical admin enter 1, for  dev admin type 2 , for dev admin type 3, for  mod admin type 4 , for helper admin type 5 ,type 6 for member, type 7 for main and  for exit:")

        if role_update=="1":
            c.execute("""UPDATE userdata SET roles = "ethical_admin"  WHERE username=?""",(username,))
            f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a")
            f.write(login_username+"change role of"+username+"to ethical_admin"+"\r\n")
            f.close()
            conect.commit()
            conect.close()


            ch=input("enter 1 if u want to see otehr things u can do  and enter 2  if u want to see exit option or option to go to main menu")

            if ch == "1":
                print("here")
            elif ch=="2":
                main()
            else:
                print ("Sorry error plz try again")
                exit()
            
        elif role_update=="2":
            c.execute("""UPDATE userdata SET roles = "dev_admin"  WHERE username=?""",(username,))
            f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a")
            f.write(login_username+"change role of"+username+"to dev_admin"+"\r\n")
            f.close()
            conect.commit()
            conect.close()


            ch=input("enter 1 if u want to see otehr things u can do  and enter 2  if u want to see exit option or option to go to main menu")
            if ch == "1":
                print("here")
            elif ch=="2":
                main()
            else:
                print ("Sorry error plz try again")
                exit()

        elif role_update=="3":
            c.execute("""UPDATE userdata SET roles = "dev"  WHERE username=?""",(username,))
            f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a")
            f.write(login_username+"change role of"+username+"to dev"+"\r\n")
            f.close()
            conect.commit()
            conect.close()


            ch=input("enter 1 if u want to see otehr things u can do  and enter 2  if u want to see exit option or option to go to main menu")
            if ch == "1":
                print("here")
            elif ch=="2":
                main()
            else:
                print ("Sorry error plz try again")
                exit()

        elif role_update=="4":
            c.execute("""UPDATE userdata SET roles = "mod"  WHERE username=?""",(username,))
            f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a")
            f.write(login_username+"change role of"+username+"to mod"+"\r\n")
            f.close()
            conect.commit()
            conect.close()


            ch=input("enter 1 if u want to see otehr things u can do  and enter 2  if u want to see exit option or option to go to main menu")
            if ch == "1":
                print("here")
            elif ch=="2":
                main()
            else:
                print ("Sorry error plz try again")
                exit()

        elif role_update=="5":
            c.execute("""UPDATE userdata SET roles = "helpers"  WHERE username=?""",(username,))
            f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a")
            f.write(login_username+"change role of"+username+"to helper"+"\r\n")
            f.close()
            conect.commit()
            conect.close()


            ch=input("enter 1 if u want to see otehr things u can do  and enter 2  if u want to see exit option or option to go to main menu")
            if ch == "1":
                print("here")
            elif ch=="2":
                main()
            else:
                print ("Sorry error plz try again")
                exit()

        elif role_update=="6":
            c.execute("""UPDATE userdata SET roles = "member"  WHERE username=?""",(username,))
            f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a")
            f.write(login_username+"change role of"+username+"to member"+"\r\n")
            f.close()
            conect.commit()
            conect.close()

            ch=input("enter 1 if u want to see otehr things u can do  and enter 2  if u want to see exit option or option to go to main menu")
            if ch == "1":
                print("here")
            elif ch=="2":
                main()
            else:
                print ("Sorry error plz try again")
                exit()
        elif role_update=="7":
            exit()
    else:
        print ("Sorry error plz try again")
        exit()

def ban_delete_user_info_1(login_username,login_password):
    print("hi")

def edit_code_databse_1(login_username,login_password):
    choice=input("Please enter 1 to if u are editing database or 2 if u are editing code or 3 for main menu  or  to  exit:")
    if choice=="1":
        tz=pytz.timezone("Europe/London")
        time=datetime.now(tz)
        time=str(time)
        f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/edit_code.txt","a")
        f.write(login_username + " "+time+"\r\n")
        f.close
        exit()
    elif choice=="2":
        tz=pytz.timezone("Europe/London")
        time=datetime.now(tz)
        time=str(time)
        f=open("C:/Users/Talha/Desktop/work/wolf-terminal/log/edit_database.txt","a")
        f.write(login_username + " "+time +"\r\n")
        f.close
        exit()
    elif choice == "3":
        ch=input("enter 1 if u want to see otehr things u can do  and enter 2  if u want to see exit option or option to go to main menu")
        if ch == "1":
            print("here")
        elif ch=="2":
            main()
        else:
            print ("Sorry error plz try again")
            exit()
    else:
        exit()

def reportbug_1(login_username,login_password):
    tz=pytz.timezone("Europe/London")
    time=datetime.now(tz)
    time=str(time)
    f=open("C:/Users/Talha/Desktop/work/wolf-terminal/sqllitesutdio work/New folder/logfile/bug_report.txt","w+")
    f.write(login_username + " "+time +"\r\n")
    f.close
    
def unban_1(login_username,login_password):
    print("hi")



def tool_sorter(role,n):
    print("hi")

def role_sorter(role,n):
    print("hi")