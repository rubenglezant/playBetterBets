import pandas as pd
import numpy as np

def crearMatriz(indice):
    f = pd.read_csv("./data/" + indice + ".csv")
    #print ("-------> Tratando el valor del INDICE -> " + indice)
    r = f[['High']]
    filasColumnas = r.index.max() + 1
    A = np.empty([filasColumnas], dtype='double')
    for i in r.index:
        valorEstudiado = r.ix[i]
        A[i] = valorEstudiado

    #print (A[1])
    return A

def analizaIndice(A, por, diasAnalisis,diaInicial):
    rows = A.shape[0]
    cuenta = 0
    for i in range(diaInicial,rows):
        valorInv = A[i]
        if (i+diasAnalisis>rows):
            break
        for j in range(i,i+diasAnalisis):
            valorAct = A[j]
            porCalculado = (valorAct - valorInv)/valorInv
            if (porCalculado>por):
                cuenta = cuenta + 1
                break
        #print (str(i)+" Valor Invertido: "+str(valorInv)+"   -> Dias "+str(j-i)+"   -> Porc "+str(porCalculado))
    porcentajeResultado = float(cuenta)/float(rows)
    #print (cuenta, rows, porcentajeResultado)
    return (porcentajeResultado,rows-diaInicial)


# MAIN
porcentajeTarget = 0.05
diasAnalisis = 20
diaInicial = 100
with open("indices.txt") as f:
    for line in f:
        indice = line.split()[0]
        A = crearMatriz(indice)
        por,totaldias = analizaIndice(A, porcentajeTarget, diasAnalisis,diaInicial)
        print (indice+" | "+str(porcentajeTarget)+" | "+str(totaldias)+" | "+str(diasAnalisis)+" | "+str(por))

