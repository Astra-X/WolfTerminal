import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from time import process_time

from login_create_account import exit
from role_sorter import *
import pytz
import sqlite3


def change_roles(login_username,login_password,sub,login_line_1,n,from_role):
    tz=pytz.timezone("Europe/London")
    time=datetime.now(tz)
    time=str(time)

    if n == " ":
        username=input("Enter usernameof svount u want  to change role of:")
        email=input("enter email:")
        conect=sqlite3.connect("C:/Users/Talha/Desktop/work/wolf-terminal/db/system_roles.db")
        c=conect.cursor()

        list_username=c.execute("SELECT username FROM unbanned_user").fetchall()
        list_username=tuple(i[0] for i in list_username)

        list_email=c.execute("SELECT email FROM unbanned_user").fetchall()
        list_email=tuple(i[0] for i in list_username)

        if username in list_username and email in list_email:
            role_update=input("do u want to update role to ethical admin enter 1, for  dev admin type 2 , for dev admin type 3, for  mod admin type 4 , for helper admin type 5 ,type 6 for member, type 7 for main and  for exit:")

            if role_update == "1":
                ch=input("enter 1 to see other tool u can access and  2 for exit and main  menu")
                c.execute("""UPDATE unbanned_user SET roles = "ethical_admin"  WHERE username=?""",(username,))

                with open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a") as f:
                    f.write(login_username +" "+time )
                    f.write(login_username+" change role of "+username+" to role_admin "+"\r\n")
                    f.close()

                with open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a") as f:
                    f.write(login_line_1)
                    f.close()
                
                conect.commit()
                conect.close()
            
            if role_update == "2":
                ch=input("enter 1 to see other tool u can access and  2 for exit and main  menu")
                c.execute("""UPDATE unbanned_user SET roles = "dev_admin"  WHERE username=?""",(username,))

                with open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a") as f:
                    f.write(login_username +" "+time )
                    f.write(login_username+" change role of "+username+" to dev_admin "+"\r\n")
                    f.close()

                with open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a") as f:
                    f.write(login_username +" "+time )
                    f.close()
                
                conect.commit()
                conect.close()

            if role_update == "1":
                ch=input("enter 1 to see other tool u can access and  2 for exit and main  menu")
                c.execute("""UPDATE unbanned_user SET roles = "ethical_admin"  WHERE username=?""",(username,))

                with open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a") as f:
                    f.write(login_username +" "+time )
                    f.write(login_username+" change role of "+username+" to dev_admin "+"\r\n")
                    f.close()

                with open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a") as f:
                    f.write(login_username +" "+time )
                    f.close()
                
                conect.commit()
                conect.close()

            if role_update == "1":
                ch=input("enter 1 to see other tool u can access and  2 for exit and main  menu")
                c.execute("""UPDATE unbanned_user SET roles = "ethical_admin"  WHERE username=?""",(username,))

                with open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a") as f:
                    f.write(login_username +" "+time )
                    f.write(login_username+" change role of "+username+" to dev_admin "+"\r\n")
                    f.close()

                with open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a") as f:
                    f.write(login_username +" "+time )
                    f.close()
                
                conect.commit()
                conect.close()

            if role_update == "1":
                ch=input("enter 1 to see other tool u can access and  2 for exit and main  menu")
                c.execute("""UPDATE unbanned_user SET roles = "ethical_admin"  WHERE username=?""",(username,))

                with open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a") as f:
                    f.write(login_username +" "+time )
                    f.write(login_username+" change role of "+username+" to dev_admin "+"\r\n")
                    f.close()

                with open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a") as f:
                    f.write(login_username +" "+time )
                    f.close()
                
                conect.commit()
                conect.close()

            if role_update == "1":
                ch=input("enter 1 to see other tool u can access and  2 for exit and main  menu")
                c.execute("""UPDATE unbanned_user SET roles = "ethical_admin"  WHERE username=?""",(username,))

                with open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a") as f:
                    f.write(login_username +" "+time )
                    f.write(login_username+" change role of "+username+" to dev_admin "+"\r\n")
                    f.close()

                with open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a") as f:
                    f.write(login_username +" "+time )
                    f.close()
                
                conect.commit()
                conect.close()

            if role_update == "1":
                ch=input("enter 1 to see other tool u can access and  2 for exit and main  menu")
                c.execute("""UPDATE unbanned_user SET roles = "ethical_admin"  WHERE username=?""",(username,))

                with open("C:/Users/Talha/Desktop/work/wolf-terminal/log/change_roles.txt","a") as f:
                    f.write(login_username +" "+time )
                    f.write(login_username+" change role of "+username+" to dev_admin "+"\r\n")
                    f.close()

                with open("C:/Users/Talha/Desktop/work/wolf-terminal/log/login.txt","a") as f:
                    f.write(login_username +" "+time )
                    f.close()
                
                conect.commit()
                conect.close()


def ban_delete_user_info(login_username,login_password,sub,login_line_1,n,from_role):
    print("hi")

def edit_code_databse(login_username,login_password,sub,login_line_1,n,from_role):
    print("hi")

def reportbug(login_username,login_password,sub,login_line_1,n,from_role):
    print("hi")



def tool_sorter(login_username,login_password,tool,n,sub,login_line_1,from_role):
    if tool =="change_roles":
        change_roles(login_username,login_password,tool,n,sub,login_line_1,from_role)
    elif tool == "ban/delete":
        ban_delete_user_info(login_username,login_password,tool,n,sub,login_line_1,from_role)
    elif tool=="edit_code_database":
        edit_code_databse(login_username,login_password,tool,n,sub,login_line_1,from_role)
    elif tool =="bug report":
        reportbug(login_username,login_password,tool,n,sub,login_line_1,from_role)
    else:
        print(" there is an error try again ")
        if from_role == "admin_ethicals":
            admin_ethicals(login_username,login_password,from_role)
        elif from_role == "admin_dev":
            dev(login_username,login_password,from_role)
        elif from_role == "dev":
            dev(login_username,login_password,from_role)
        elif from_role == "mod":
            mod(login_username,login_password,from_role)
        elif from_role == "helpers":
            helpers(login_username,login_password,from_role)
        else:
            print(" there is an error try again ")
            exit()



superviosrname=c.execute("""SELECT supervisor_name  FROM bill_detail WHERE bill_nr =? """,(listbranchcode[0],)).fetchall()

superviosrid=c.execute("""SELECT supervisor_id  FROM bill_detail WHERE bill_nr =? """,(listbranchcode[0],)).fetchall()

print(superviosrid[0]+superviosrname[0])