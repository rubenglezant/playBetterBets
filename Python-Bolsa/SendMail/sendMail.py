__author__ = 'ruben'

import smtplib
import time
import MySQLdb

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

s = "Text plain"
html = ""
with open('newsletter.html') as f:
	for line in f:
		html += line;

# Recuperamos los correos de la BBDD
toaddrs  = []

with open('correos.txt') as fp:
    for line in fp:
        print line
	toaddrs.append(line)

#toaddrs  = ['pcillo2mar@gmail.com','ruben_gonzalez@iecisa.com']


# Record the MIME types of both parts - text/plain and text/html.
part1 = MIMEText("", 'plain')
part2 = MIMEText(html, 'html')

fecha = (time.strftime("%d/%m/%y"))
fromaddr = 'pcillo2mar@gmail.com'

for destino in toaddrs:
	msg = MIMEMultipart('alternative')
	msg['Subject'] = "x0m0x - "+fecha+" - x0m0x"
	msg['From'] = fromaddr
	msg['To'] = " "
	msg.attach(part1)
	msg.attach(part2)
	username = 'pcillo2mar@gmail.com'
	password = '4c1TNRdi'
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.ehlo()
	server.starttls()
	server.login(username,password)
	#server.sendmail(me, you, msg.as_string())
	server.sendmail(fromaddr, destino, msg.as_string())
	server.quit()
