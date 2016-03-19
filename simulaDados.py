import random
import sys

# Principal
for juegos in range(1,30):
    pastaTotal = 200
    pasta = 1
    direccion = 0
    limite = 49.5
    balanceUser = "0"
    numeroPerdidas = 0
    limitePerdidas = 3
    for i in range(1,2000):
        # Arruinado
        if (pasta > pastaTotal):
            # print (str(juegos)+"\t\t"+"0"+"\t\t"+"-100.0")
            break
        # Lanzamos los dados
        dado = random.uniform(0, 100)
        if (dado > limite):
            pastaTotal += pasta
        else:
            pastaTotal -= pasta
        #print response.text
        #print (str(i)+"\t\t"+str(pastaTotal))
        # Estrategia
        if (dado <= limite):
            numeroPerdidas += 1
        else:
            numeroPerdidas = 0
        if (numeroPerdidas>=limitePerdidas):
            pasta *= 2
            #print ("Correctivo:" + str(pasta))
        else:
            pasta = 1
        sys.stdout.flush()
    print (str(juegos)+"\t\t"+str(pastaTotal)+"\t\t"+str(float((pastaTotal-200)*100)/200))


