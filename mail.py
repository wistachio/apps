import smtplib
import poplib

usr = 'me.abstract.9@gmail.com'
pwd = 'abstraction9'

def send(subject,body,addr):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login(usr,pwd)

    subject = subject
    body = body

    msg = f'Subject: {subject}\n{body}'

    x = server.sendmail(usr, addr, msg)
    print('Email sent')

    server.quit()

def recv():
    m = poplib.POP3('localhost')
    m.user(usr)
    m.pass_(pwd)
    print(m.list())

