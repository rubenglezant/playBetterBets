from __future__ import division

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

# CRITERIO INVERSION: Ninguno
def calculaInd1(indice, diasVentana, porcentajeGanar):
    A = np.loadtxt(indice+'-matriz_porcentajes.dat')

    # Ajustamos la matriz a dias de ventana
    maxX,maxY = A.shape
    for i in range(0,maxX):
        for j in range(0, maxY):
            if ((i+diasVentana)<j):
                A[i][j] = 0

    try:
        j = 0
        gan = 0
        for i in A:
            j = j + 1
            if (i.max()>porcentajeGanar):
                #print(j, i.max(), i.min())
                gan = gan + 1

        if (A.max()>0):
            print("=" + str(gan) + "/" + str(j));
            #print (indice, (gan/j), gan, j, porcentajeGanar, diasVentana);
    except:
        pass

    return

# CRITERIO INVERSION: Solo invierto tras dos bajadas consecutivas
# Este criterio no es muy bueno, funciona peor que tras una bajada
def calculaInd2(indice, diasVentana, porcentajeGanar):
    A = np.loadtxt(indice+'-matriz_porcentajes.dat')

    # Ajustamos la matriz a dias de ventana
    maxX,maxY = A.shape
    for i in range(0,maxX):
        for j in range(0, maxY):
            if ((i+diasVentana)<j):
                A[i][j] = 0
    A = A[0:(maxX-diasVentana)][:]

    #print (A[421])
    #print(A.shape)
    j = 0
    gan = 0
    inver = 0
    for i in A:
        if ((j+3)<maxY):
            if (((A[j][j+1])<0) and ((A[j][j+1])>(A[j][j+2]))):
            #if ((A[j][j + 1]) < 0):
                inver = inver + 1
                if (i.max()>porcentajeGanar):
                    gan = gan + 1
            j = j + 1

    if (inver>0):
        print (indice, (gan/inver), gan, inver, porcentajeGanar, diasVentana);
    else:
        print(indice,  gan, inver, porcentajeGanar, diasVentana);

    return

# CRITERIO INVERSION: Solo invierto tras TRES SUBIDAS consecutivas
# Funciona mejor que ante las bajadas
def calculaInd3(indice, diasVentana, porcentajeGanar):
    A = np.loadtxt(indice+'-matriz_porcentajes.dat')

    # Ajustamos la matriz a dias de ventana
    maxX,maxY = A.shape
    for i in range(0,maxX):
        for j in range(0, maxY):
            if ((i+diasVentana)<j):
                A[i][j] = 0
    A = A[0:(maxX-diasVentana),:]
    A = A[0:,0:]

    #print (A[421])
    #print(A.shape)
    j = 0
    gan = 0
    inver = 0
    for i in A:
        if ((j+4)<maxY):
            if (((A[j][j+1])>0) and ((A[j][j+1])<(A[j][j+2])) and ((A[j][j + 2]) < (A[j][j + 3]))):
            #if ((A[j][j + 1]) < 0):
                inver = inver + 1
                if (i.max()>porcentajeGanar):
                    gan = gan + 1
            j = j + 1

    if (inver>0):
        #print (indice, (gan/inver), gan, inver, porcentajeGanar, diasVentana);
        print ("="+str(gan)+"/"+str(inver));
    else:
        print(indice,  gan, inver, porcentajeGanar, diasVentana);

    return

# CRITERIO INVERSION: Cuando baje de la media de los ultimos 10 dias
# Tampoco esta funcionando especialmente bien
def calculaInd4(indice, diasVentana, porcentajeGanar, diasMedia):
    A = np.loadtxt(indice+'-matriz_porcentajes.dat')

    # Ajustamos la matriz a dias de ventana
    maxX,maxY = A.shape
    for i in range(0,maxX):
        for j in range(0, maxY):
            if ((i+diasVentana)<j):
                A[i][j] = 0
    A = A[0:(maxX-diasVentana)][:]

    #print (A[421])
    #print(A.shape)
    j = 0
    gan = 0
    inver = 0
    for i in A:
        if (j>diasMedia):
            media = A[j-diasMedia][0:j+1].mean()
            if (((A[j][j+1])<media)):
                #if ((A[j][j + 1]) < 0):
                inver = inver + 1
                if (i.max()>porcentajeGanar):
                    gan = gan + 1
        j = j + 1

    if (inver>0):
        #print (indice, (gan/inver), gan, inver, porcentajeGanar, diasVentana, diasMedia);
        print ((gan/inver));
    else:
        print(indice,  gan, inver, porcentajeGanar, diasVentana, diasMedia);

    return

# Realizamos el calculo para todos los indices
with open("indices.txt") as f:
    for line in f:
        indice = line.split()[0]
        for i in range(0,1):
            calculaInd3(indice,100,0.077-0.015*i)
            #calculaInd1(indice, 100, 0.087)
            #calculaInd1(indice, 100 + 10 * i, 0.01)


		
