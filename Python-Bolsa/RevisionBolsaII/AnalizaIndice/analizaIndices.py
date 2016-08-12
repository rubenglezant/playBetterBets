from __future__ import division

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

def calculaInd1(indice):
    porcentajeGanar = 0.10

    A = np.loadtxt(indice+'-matriz_porcentajes.dat')

    # Obtenemos el primer anno 2006
    numeroFilaAnno = 260
    # Dias de Desplazamiento sobre el annoo
    anno = 2607-260
    try:
        A = A[anno:numeroFilaAnno+anno,anno:numeroFilaAnno+anno]

        j = 0
        gan = 0
    #    print A
        for i in A:
            j = j + 1
            if (i.max()>porcentajeGanar):
                #print(j, i.max(), i.min())
                gan = gan + 1

        if (A.max()>0):
            print (indice,A.max(), A.min(), A.mean(), (gan/j));
    except:
        pass

    return

# Comprobamos las caidas continuas
def calculaInd2(indice):
    A = np.loadtxt(indice+'-matriz_porcentajes.dat')
    # Obtenemos el ultimo anno
    numeroFilaAnno = 260
    # Dias de Desplazamiento sobre el annoo
    anno = 2607-260

    #A = A[anno:numeroFilaAnno+anno,anno:numeroFilaAnno+anno]

    caidaMax = 0
    for i in range(0,numeroFilaAnno-1):
        valorAnt = +1000
        caida = 0
        for j in range(0,numeroFilaAnno-1):
            valor = A[i,j]
            if (valorAnt<valor):
                caida = caida + 1
            else:
                #print i,j,caida
                if (caida>caidaMax):
                    caidaMax = caida
                caida = 0
            valorAnt = valor

    print (indice, caidaMax)

    return

# Buscamos el mejor porcenjate de salida dentro de los posibles
def calculaInd3(indice):
    porcentajeGanar = 0.05

    A = np.loadtxt(indice+'-matriz_porcentajes.dat')

    # Obtenemos el primer anno 2006
    numeroFilaAnno = 260
    # Dias de Desplazamiento sobre el annoo
    anno = 2607-260
    try:

        A = A[anno:numeroFilaAnno+anno,anno:numeroFilaAnno+anno]

        ListaValores = []
        for bucle in range(0,20):
            j = 0
            gan = 0
            for i in A:
                j = j + 1
                if (i.max()>porcentajeGanar):
                    gan = gan + 1
            if (A.max()>0):
                ListaValores.append((gan/j))
            porcentajeGanar = porcentajeGanar + 0.005

        print (indice, ListaValores)
    except:
        pass

    return

# Buscamos el mejor porcenjate de salida dentro de los posibles
def calculaInd4(indice):
    porcentajeGanar = 0.05

    A = np.loadtxt("./data/"+indice+'-matriz_porcentajes.dat')

    try:
        ListaValores = []
        for bucle in range(0,20):
            j = 0
            gan = 0
            for i in A:
                j = j + 1
                if (i.max()>porcentajeGanar):
                    gan = gan + 1
            if (A.max()>0):
                ListaValores.append((gan/j))
            porcentajeGanar = porcentajeGanar + 0.005

        print (indice, ListaValores)
    except:
        pass

    return

# Buscamos el mejor porcenjate de salida dentro de los posibles
# Tomamos una ventana de X dias para que la comparativa sea buena
def calculaInd5(indice,dias,ultimodia):
    A = np.loadtxt("./data/"+indice+'-matriz_porcentajes.dat')

    # Tomamos una ventana de 20 dias, excepto el dia anterior
    diasVentana = ((-1)*(dias*dias+ultimodia))
    B = A[diasVentana:(-1)*ultimodia,diasVentana:(-1)*ultimodia]
    row,col = B.shape
    # Ahora vamos a poner los ceros adicionales
    for i in range (0,dias*2):
        for j in range (dias+i,col):
            B[i,j] = 0
    B = B[0:dias*2,:]
    print (B)
    print ("Maxima Ganancia " + str(B.max()))
    print ("Maxima Perdida " + str(B.min()))

    np.savetxt("./data/"+indice+'-test.dat', B, fmt='%.2e')

    return

# Buscamos el mejor porcenjate de salida dentro de los posibles
# Tomamos una ventana de X dias para que la comparativa sea buena
def calculaInd6(indice,dias,ultimodia,porcentajeTarget):
    A = np.loadtxt("./data/"+indice+'-matriz_porcentajes.dat')

    # Tomamos una ventana de 20 dias, excepto el dia anterior
    diasVentana = ((-1)*(dias*2+ultimodia))
    B = A[diasVentana:,diasVentana:]
    B = B[0:dias,0:dias*2]
    row,col = B.shape
    # Ahora vamos a poner los ceros adicionales
    for i in range (0,dias*2):
        for j in range (dias+i,col):
            B[i,j] = 0
    # En la nueva matriz calculamos el porcentaje de ganar
    row,col = B.shape
    conseguido = 0
    for i in range (0,row):
        for j in range (0,col):
            if (B[i,j]>=porcentajeTarget):
                conseguido = conseguido + 1
                break

    #for i in range (0,row):
    #    print (i, B[i,:].max())

    np.savetxt("./data/"+indice+'-matriz_test.dat', B, fmt='%.2e')

    return (porcentajeTarget,conseguido,row)

def analizaIndice(indice,por):
    cont = 0
    total = 0.0
    for i in range(40,12*20):
        (porcentajeTarget,a,b) = calculaInd6(indice,40,i,por)
        total = (a/b) + total
        cont = cont + 1
    print (indice,porcentajeTarget,total/cont)


# Realizamos el calculo para todos los indices
por = 0.07
with open("indices.txt") as f:
    for line in f:
        indice = line.split()[0]
        try:
            analizaIndice(indice,por)
        except:
            pass


		
