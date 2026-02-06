# works with Less Secure app which is disbale from January 2025
# this code is just a basic idea for future develoment

import smtplib

to = input("Enter the recipent email: ")
content = input("Write the content of the email: ")

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 578)
    server.ehlo()
    server.starttls()
    server.login('senderemail@gmail.com','1234')
    server.sendmail('senderemail@gmail.com',to,content)
    server.close()
    
sendEmail(to,content)