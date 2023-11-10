import requests
import time
import smtplib

userpass = open("userpass.txt", "r")

for x in userspass.items():
  time.sleep(2)
  sendMail()
  
def sendMail():
    try:
        server_ssl = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server_ssl.ehlo()
        server_ssl.login(x[0],x[1])
        print("connected!",x[0],":",x[1])
    except:
        print('Incorrect',x[0],":",x[1])
