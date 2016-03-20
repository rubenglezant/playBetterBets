import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

with open("indices.txt") as f:
    for line in f:
        indice = line.split()[0]
        # Obtenemos los datos del indice
        f = pd.read_csv(indice+'.csv')
        print (indice)
        print (f[:2])

        r = f[['Open']]

        # Creamos la matriz de porcentajes
        # Tanto las filas como las columnas son los dias de cotizacion
        filasColumnas = r.index.max() + 1
        matrizPorcentajes = np.empty([filasColumnas,filasColumnas],dtype='double')

        for i in r.index:
            valorEstudiado = r.ix[i]
            for j in r.index:
                if (j<i):
                    matrizPorcentajes[i,j] = 0
                else:
                    matrizPorcentajes[i,j] = ((r.ix[j]-valorEstudiado)/valorEstudiado)

        np.savetxt(indice+'-matriz_porcentajes.dat', matrizPorcentajes, fmt='%.4e')
