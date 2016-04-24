from scipy.stats._discrete_distns import poisson_gen

__author__ = 'ruben'

import smtplib
import time
import pandas.io.data as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import sys

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviaMail(cadena):
    s = "Text plain"
    html = cadena
    toaddrs  = ['pcillo2mar@gmail.com','ruben_gonzalez@iecisa.com']

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText("", 'plain')
    part2 = MIMEText(html, 'html')

    fecha = (time.strftime("%d/%m/%y"))
    fromaddr = 'pcillo2mar@gmail.com'

    for destino in toaddrs:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = cadena
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
    return

lista_indices = ["GAM.MC","AENA.MC","BKT.MC"]

for indice in lista_indices:
    ahora = datetime.datetime.now()

    start = datetime.datetime(2016, 1, 1)
    end = datetime.datetime(2016, ahora.month, ahora.day)

    f = web.DataReader(indice, 'yahoo', start, end)

    f = (f["Close"])

    if (((f.ix[-1])>(f.ix[-2])) and ((f.ix[-2])>(f.ix[-3]))):
        print "Sube 3 veces " + indice
        enviaMail("Sube 3 veces " + indice)
    else:
        print "NO Sube " + indice
        enviaMail("NO Sube " + indice)

print ""
# Valoracion de las inversiones realizadas
indice = "GAM.MC"
fechaInversion = '2016-03-31'
start = datetime.datetime(2016, 03, 31)

end = datetime.datetime(2016, ahora.month, ahora.day)
f = web.DataReader(indice, 'yahoo', start, end)
f = (f["High"])
ValorInversion = f.ix[fechaInversion]
porcentajeMax = -1;
print "Estas invirtiendo en " + indice + " a " + str(ValorInversion) + " en fecha " + fechaInversion
print ""
for date, row in f.T.iteritems():
   valorAct = row
   porcentaje = (valorAct - ValorInversion)/ValorInversion;
   print date,row, porcentaje
   if (porcentaje>porcentajeMax):
       porcentajeMax = porcentaje;

print ""
print "Mejor rentabilidad " + indice + " es " + str(porcentajeMax)
print "-----------------------------------------------------------"

# Valoracion de las inversiones realizadas
indice = "AENA.MC"
fechaInversion = '2016-04-06'
start = datetime.datetime(2016, 04, 06)

end = datetime.datetime(2016, ahora.month, ahora.day)
f = web.DataReader(indice, 'yahoo', start, end)
f = (f["High"])
ValorInversion = f.ix[fechaInversion]
porcentajeMax = -1;
print "Estas invirtiendo en " + indice + " a " + str(ValorInversion) + " en fecha " + fechaInversion
print ""
for date, row in f.T.iteritems():
   valorAct = row
   porcentaje = (valorAct - ValorInversion)/ValorInversion;
   print date,row, porcentaje
   if (porcentaje>porcentajeMax):
       porcentajeMax = porcentaje;

print ""
print "Mejor rentabilidad " + indice + " es " + str(porcentajeMax)
print "-----------------------------------------------------------"

# Valoracion de las inversiones realizadas
indice = "BKT.MC"
fechaInversion = '2016-04-15'
start = datetime.datetime(2016, 04, 15)

end = datetime.datetime(2016, ahora.month, ahora.day)
f = web.DataReader(indice, 'yahoo', start, end)
f = (f["High"])
ValorInversion = f.ix[fechaInversion]
porcentajeMax = -1;
print "Estas invirtiendo en " + indice + " a " + str(ValorInversion) + " en fecha " + fechaInversion
print ""
for date, row in f.T.iteritems():
   valorAct = row
   porcentaje = (valorAct - ValorInversion)/ValorInversion;
   print date,row, porcentaje
   if (porcentaje>porcentajeMax):
       porcentajeMax = porcentaje;

print ""
print "Mejor rentabilidad " + indice + " es " + str(porcentajeMax)
print "-----------------------------------------------------------"







