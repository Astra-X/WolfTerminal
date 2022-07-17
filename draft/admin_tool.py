import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime
from time import process_time

from regex import P
from login_create_account import *
import pytz
import os
import sqlite3



def dev(login_username,login_password):


    choice=input("enter 1 to edit code and data base, enter 2 for going to main menu or exit program:")
    if choice == "1":
        edit_code_databse(login_username,login_password)
    elif choice == "2":
        exit()
    else:
        dev(login_username,login_password)

def mod(login_username,login_password):

    choice=input("enter 1 to ban/delete user info  , enter 2 for going to main menu or exit program:")
    if choice == "1":
        ban_delete_user_info(login_username,login_password)
    elif choice == "2":
        exit()
    else:
        mod(login_username,login_password)

def helpers(login_username,login_password):

    choice=input("enter 1 to reprt bug , enter 2 for going to main menu or exit program:")
    if choice == "1":
        reportbug(login_username,login_password)
    elif choice == "2":
        exit()
    else:
        helpers(login_username,login_password)

def member(login_username,login_password):
    print("hi")





def change_roles(login_username,login_password):
    print("hi")

def ban_delete_user_info(login_username,login_password):
    print("hi")

def edit_code_databse(login_username,login_password):
    print("hi")

def reportbug(login_username,login_password):
    print("hi")

def unban(login_username,login_password):
    print("hi")

def tool_sorter(login_username,login_password,tool,n,sub):
    print("hi")
