
from datetime import datetime
from time import process_time
from login_create_account import exit
from admintools import tool_sorter
import pytz


def admin_ethicals(login_username,login_password,from_role):
    print("enter 1 to change roles, enter 2 to ban/delete/unban user or user info , 3 for going to main menu or exit program:")
    choice =input(":")

    if choice== "1":
        tz=pytz.timezone("Europe/London")
        time=datetime.now(tz)
        time=str(time)
        
        login_line_1=login_username + " "+time+"\r\n"
        tool="change_roles"
        n=" "
        sub=" "


        tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role)

    elif choice == "2":
        print("enter 1 to delete user info or 2 for to move them to ban list or 3 to unban or 4 to see other tools u can acces or 5 for going to main menu or exit program:")
        choice=input(":")

        if choice == "1":
            tz=pytz.timezone("Europe/London")
            time=datetime.now(tz)
            time=str(time)
            
            login_line_1=login_username + " "+time+"\r\n"
            tool="ban/delete"
            n=" "
            sub="delete"


            tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role)


        elif choice == "2":
            tz=pytz.timezone("Europe/London")
            time=datetime.now(tz)
            time=str(time)

            login_line_1=login_username + " "+time+"\r\n"
            tool="ban/delete"
            n=" "
            sub="ban"


            tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role)

        elif choice == "3":
            tz=pytz.timezone("Europe/London")
            time=datetime.now(tz)
            time=str(time)

            login_line_1=login_username + " "+time+"\r\n"
            tool="ban/delete"
            n=" "
            sub="unban"


            tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role)

        elif choice == "4":
            admin_ethicals(login_username,login_password,from_role)
        
        elif choice == "5":
            exit()
        
        else:
            admin_ethicals(login_username,login_password,from_role)
    
    elif choice == "3":
        exit()
    
    else: 
        admin_ethicals(login_username,login_password,from_role)
        
def admin_dev(login_username,login_password,from_role):
    print("enter 1 to change roles, enter 2 to ban/delete/unban user info , 3 for edit code and data base , 4 for going to main menu or exit program:")
    choice=input(":")

    if choice == "1":
        tz=pytz.timezone("Europe/London")
        time=datetime.now(tz)
        time=str(time)
        
        login_line_1=login_username + " "+time+"\r\n"
        tool="change_roles"
        n=" "
        sub=" "

        tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role)

    elif choice == "2":
        print("enter 1 to delete user info or 2 for to move them to ban list or 3 to unban or 4 to see other tools u can acces or 5 for going to main menu or exit program:")
        choice=input(":")

        if choice == "1":
            tz=pytz.timezone("Europe/London")
            time=datetime.now(tz)
            time=str(time)

            login_line_1=login_username + " "+time+"\r\n"
            tool="ban/delete"
            n=" "
            sub="delete"
    

            tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role)

        elif choice == "2":
            tz=pytz.timezone("Europe/London")
            time=datetime.now(tz)
            time=str(time)

            login_line_1=login_username + " "+time+"\r\n"
            tool="ban/delete"
            n=" "
            sub="ban"


            tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role)

        elif choice == "3":
            tz=pytz.timezone("Europe/London")
            time=datetime.now(tz)
            time=str(time)

            
            login_line_1=login_username + " "+time+"\r\n"
            tool="ban/delete"
            n=" "
            sub="unban"

            tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role)


        elif choice == "4":
            admin_dev(login_username,login_password,from_role)
        
        elif choice == "5":
            exit()
        
        else:
            admin_dev(login_username,login_password,from_role)

    elif choice =="3":
        print ("enter 1 if u  will edit code , enter 2 if u will edit database , enter 3 for other tools u can acces or 4 to exit or to go to main menu:")
        choice=input(":")

        if choice == "1":
            tz=pytz.timezone("Europe/London")
            time=datetime.now(tz)
            time=str(time)
            
            login_line_1=login_username + " "+time+"\r\n"
            tool="edit_code_database"
            n=" "
            sub="code"

            tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role)

        elif choice == "2":
            tz=pytz.timezone("Europe/London")
            time=datetime.now(tz)
            time=str(time)
            
            login_line_1=login_username + " "+time+"\r\n"
            tool="edit_code_database"
            n=" "
            sub="database"


            tool_sorter(login_username,login_password,tool,n,sub,from_role)
        
        elif choice == "3":
            admin_dev(login_username,login_password,from_role)
        
        elif choice == "4":
            exit()
        
        else:
            admin_dev(login_username,login_password,from_role)

    elif choice == "4":
        exit()

    else:
        admin_dev(login_username,login_password,from_role)

def dev(login_username,login_password,from_role):
    print("enter 1 to edit code and data base, enter 2 for going to main menu or exit program:")
    choice=input(":")
    
    if choice == "1":
        print ("enter 1 if u  will edit code , enter 2 if u will edit database , enter 3 for other tools u can acces or 4 to exit or to go to main menu:")
        choice=input(":")

        if choice == "1":
            tz=pytz.timezone("Europe/London")
            time=datetime.now(tz)
            time=str(time)
            
            login_line_1=login_username + " "+time+"\r\n"
            tool="edit_code_database"
            n=" "
            sub="code"


            tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role)


        elif choice == "2":
            tz=pytz.timezone("Europe/London")
            time=datetime.now(tz)
            time=str(time)
            
            login_line_1=login_username + " "+time+"\r\n"
            tool="edit_code_database"
            n=" "
            sub="database"


            tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role)

        
        elif choice == "3":
            dev(login_username,login_password,from_role)
        
        elif choice == "4":
            exit()
        
        else:
        
            dev(login_username,login_password,from_role)

    elif choice == "2":
        exit()
    
    else:
        dev(login_username,login_password,from_role)

def mod(login_username,login_password,from_role):
    
    choice=input("enter 1 to ban/delete user info  , enter 2 for going to main menu or exit program:")
    if choice == "1":
        print("enter 1 to delete user info or 2 for to move them to ban list or 3 to unban or 4 to see other tools u can acces or 5 for going to main menu or exit program:")
        choice=input(":")

        if choice == "1":
            tz=pytz.timezone("Europe/London")
            time=datetime.now(tz)
            time=str(time)

            login_line_1=login_username + " "+time+"\r\n"
            tool="ban/delete"
            n=" "
            sub="delete"

            tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role)


        elif choice == "2":
            tz=pytz.timezone("Europe/London")
            time=datetime.now(tz)
            time=str(time)

            login_line_1=login_username + " "+time+"\r\n"
            tool="ban/delete"
            n=" "
            sub="ban"

            tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role)

        elif choice == "3":
            tz=pytz.timezone("Europe/London")
            time=datetime.now(tz)
            time=str(time)

            
            login_line_1=login_username + " "+time+"\r\n"
            tool="ban/delete"
            n=" "
            sub="unban"


            tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role)

        elif choice == "4":
            mod(login_username,login_password,from_role)
        
        elif choice == "5":
            exit()
        
        else:
            mod(login_username,login_password,from_role)

    elif choice == "2":
        exit()

    else:
        mod(login_username,login_password,from_role)

def helpers(login_username,login_password,from_role):
    print("enter 1  if want to report bug ,enter 2 to drr other tool u can use and 3 for main menu or exit exit option:")
    if choice=="1":
        choice=input(":")
        tz=pytz.timezone("Europe/London")
        time=datetime.now(tz)
        time=str(time)
        
        login_line_1=login_username + " "+time+"\r\n"
        tool="bug report"
        n=" "
        sub=" "


        tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role)
    
    elif choice=="2":
        helpers(login_username,login_password,from_role)

    elif choice=="3":
        exit()

    else:
        helpers(login_username,login_password,from_role)

def member(login_username,login_password,from_role):
    print("you can oly acces resources")




