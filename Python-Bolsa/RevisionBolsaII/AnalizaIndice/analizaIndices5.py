from datetime import datetime
import pandas.io.data as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def valoraInversion(indice,porcentajeGanar, fechaInicio, fechaFin, criterio, precioSinCriterio):
    #Parametros
    #indice = "GAM.MC"
    #porcentajeGanar = 0.070
    #criterio = 1;
    # 0 - Ningun Criterio
    # 1 - Tres subidas consecutivas

    # Recogemos los valores del indice para el test
    start = datetime.strptime(fechaInicio, '%d/%m/%Y')
    end = datetime.strptime(fechaFin, '%d/%m/%Y')
    f = web.DataReader(indice, 'yahoo', start, end)

    print (f)

    # Lo incluimos en un array de double
    r = f[['High']]
    filasColumnas = r.values.size
    matrizIndice = np.empty([filasColumnas], dtype='double')
    for i in range(0,filasColumnas):
        valorEstudiado = r.values[i]
        matrizIndice[i] = valorEstudiado

    # Recorremos todas las subidas 3 veces en el periodo
    listaDias = []
    listaPrecioCompra = []
    print("Indice: " + indice);
    if (criterio==1):
        precioCompraIndice = 0
        for i in range(0, filasColumnas-2):
            valorEstudiado = matrizIndice[i]
            if ((valorEstudiado<matrizIndice[i+1]) and (matrizIndice[i+1]<matrizIndice[i+2])):
                precioCompraIndice = matrizIndice[i+2]
                diaDeCompra = i+2
                listaDias.append(diaDeCompra)
                listaPrecioCompra.append(precioCompraIndice)
    else:
        precioCompraIndice = precioSinCriterio

    print (listaPrecioCompra)
    print (listaDias)

    # Una vez que las listas estan completas, vamos a analizar cada caso
    listaGanados = []
    listaDiaVenta = []
    for diaCompra in listaDias:
        ganado = 0
        precioCompraIndice = matrizIndice[diaCompra]
        for i in range(diaCompra,filasColumnas):
            valorEstudiado = matrizIndice[i]
            porcentaje = 1 - (precioCompraIndice/valorEstudiado)
            if (porcentaje>porcentajeGanar):
                #print ("Porcentaje Venta: "+str(porcentaje));
                #print ("Precio Venta: "+str(valorEstudiado));
                #print ("GANAS: SI! en dia "+str(i));
                ganado = ganado + 1
                break
        listaGanados.append(ganado)
        listaDiaVenta.append(str(i))

    print (listaGanados)
    print (listaDiaVenta)

    ganado = 0
    for i in listaGanados:
        if (i==1):
            ganado = ganado + 1
    print (ganado)
    print ((float(ganado)/len(listaGanados)))

    # Escribimos los resultados
    s = "" + indice +"|" + fechaInicio +"|" + fechaFin +"|" + str(porcentajeGanar) +"|" + str((float(ganado)/len(listaGanados)))
    with open("resultados.txt", "a") as myfile:
        myfile.write(s+"\n")


# Main
with open("indices.txt") as f:
    for line in f:
        indice = line.split()[0]
        valoraInversion(indice,0.07,"01/03/2016","01/09/2016",1,0)
