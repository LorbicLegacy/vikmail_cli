import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import sys
file = open("loginfile.txt","r")
login = []
for line in file:
    login.append(line)
file.close()

email_user = login[0]           #sender account
email_password = login[1]       #sender password
email_send = input("Enter receivers email address : ")  #receiver account

subject = input("Enter subject : ")

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = input("Enter message : ")
msg.attach(MIMEText(body,'plain'))

ask_file = input("Do you want to send file (Y/N) : ")

if  ask_file.lower() == 'y':

    filename=input("Enter file path : ")
    filename.replace("\\","\\\\")
    attachment  = open(filename,'rb')

    part = MIMEBase('application','octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition',"attachment; filename= "+filename)

    msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
print("Starting server...")
server.starttls()
print("Logging in...")
server.login(email_user,email_password)
print("Sending Email...")
server.sendmail(email_user,email_send,text)

print("Email sent.")
server.quit()
