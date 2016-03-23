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

# Realizamos el calculo para todos los indices
with open("indices.txt") as f:
    for line in f:
        indice = line.split()[0]
        try:
            calculaInd3(indice)
        except:
            pass


		
