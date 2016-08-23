from random import randint
import sys

# Principal
BTs = int(sys.argv[1])
Llamadas = int(sys.argv[2])
IMEIs = int(sys.argv[3])
a = ""
for x in range(0,1):
    for j in range(0,BTs):
        for i in range(0,Llamadas):
            valor = (randint(0,IMEIs))
            a += "IMEI" + (str(valor).zfill(12))
            a += ("|")
            valor = (randint(0,BTs))
            a += "BT" + (str(valor).zfill(12))
            a += ("|")
            valor = (randint(0,1440))
            a += (str(valor).zfill(12))
            a += ("\r\n")
            sys.stdout.write(a)
            a = ""
        sys.stdout.flush()




