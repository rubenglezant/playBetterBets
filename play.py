import requests
import sys

# Principal
pasta = 0.00000050
direccion = 0
balanceUser = "0"
numeroPerdidas = 3
for i in range(1,1000):
    # Lanzamos los dados
    datos = {
       "accessToken": "8ff2dc9da9c263242a0d2a782fba0d486112451f6a9417410b7347cb53593d0d",
       "wager": str(pasta),
       "chance": "49.5",
       "direction": str(direccion)
    }

    url = "https://betterbets.io/api/betDice/"
    response = requests.post(url, data=datos)
    respJson = response.json()
    #print response.text
    print ("\t\t"+respJson['balanceOrig']+"\t\t"+respJson['balance']+"\t\t"+respJson['win'])
    # Estrategia
    if (respJson['win']=="0"):
        numeroPerdidas += 1
    else:
        numeroPerdidas = 0
    if (numeroPerdidas>=3):
        pasta *= 2
        print ("Correctivo:" + str(pasta))
    else:
        pasta = 0.00000050
    # Si ganamos lo esperado se termino.
    if (float(respJson['balance']) >= 0.00003000):
        break;
    sys.stdout.flush()
