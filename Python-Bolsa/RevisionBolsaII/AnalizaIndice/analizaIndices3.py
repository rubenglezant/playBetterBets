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

def seleccionaValor(A):
    return A[320-40:].mean()

def analizaIndice(A, por, diasAnalisis,diaInicial,valorInversion):
    rows = A.shape[0]
    cuenta = 0
    cuentaTotal = 0
    for i in range(diaInicial,rows):
        valorInv = A[i]
        # Solo invertimos si el valor de la inversion es menor que el seleccionado por parametro
        if (valorInv>=valorInversion):
            break
        # Si no hay filas suficientes para llegar a los diasAnalisis, no se realiza la prueba
        if (i+diasAnalisis>rows):
            break
        # CuentaTotal indica los indices que se pruebas
        cuentaTotal = cuentaTotal + 1
        for j in range(i,i+diasAnalisis):
            valorAct = A[j]
            porCalculado = (valorAct - valorInv)/valorInv
            if (porCalculado>por):
                # Cuenta indica los indices que si generan la ganancia esperada (porcentaje)
                cuenta = cuenta + 1
                break
        #print (str(i)+" Valor Invertido: "+str(valorInv)+"   -> Dias "+str(j-i)+"   -> Porc "+str(porCalculado))
    if (cuentaTotal<=0):
        porcentajeResultado = 0
    else:
        porcentajeResultado = float(cuenta)/float(cuentaTotal)
    #print (cuenta, rows, porcentajeResultado)
    return (porcentajeResultado,rows-diaInicial,cuentaTotal)


# MAIN
porcentajeTarget = 0.07
diasAnalisis = 40
diaInicial = 100
with open("indices.txt") as f:
    for line in f:
        indice = line.split()[0]
        A = crearMatriz(indice)
        valorSel = seleccionaValor(A)
        por,totaldias,totalinversiones = analizaIndice(A, porcentajeTarget, diasAnalisis,diaInicial,valorSel)
        print (indice+" | "+str(porcentajeTarget)+" | "+str(totaldias)+" | "+str(totalinversiones)+" | "+str(diasAnalisis)+" | "+str(valorSel)+" | "+str(por))

