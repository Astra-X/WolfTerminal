from logging import exception
import re
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pandas as pd

def send_email(user,pwd,subject):
    try:
        d={"col1":[1,2],"col1":[3,4]}
        df=pd.DataFrame(d)
        df_html=df.to_html()
        dfpart=MIMEText(df_html,"html")

        recipients=["talhhasber14@gmail.com","hi"]

        msg = MIMEMultipart("alternative")
        msg['From'] = user
        msg['To'] = ",".join(recipients)
        msg['Subject'] = subject
        msg.attach(dfpart)
        server=smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login(user,pwd)
        
        server.sendmail(user,recipients,msg.as_string())
        server.close()
        
        print("sent")
    except exception as e:
        print (str(e))
        print("failed")
    
    send_email("noreplyresit@gmail.com","aQW8m7WcKTK*NpA4m-@D_$#AT8rE7MSS9m*NS?7wv?_Bbd-GEnu3MrABqY+@23FXeA","frank email")