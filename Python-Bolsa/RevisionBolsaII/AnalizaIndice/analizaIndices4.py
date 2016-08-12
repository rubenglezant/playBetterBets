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

    # Decision del metodo de inversion y valoracion
    print("Indice: " + indice);
    if (criterio==1):
        precioCompraIndice = 0
        for i in range(0, filasColumnas-2):
            valorEstudiado = matrizIndice[i]
            if ((valorEstudiado<matrizIndice[i+1]) and (matrizIndice[i+1]<matrizIndice[i+2])):
                precioCompraIndice = matrizIndice[i+2]
                break
    else:
        precioCompraIndice = precioSinCriterio

    diaCompra = i+2
    print("Dia Compra: " + str(diaCompra));
    print("Precio Compra: " + str(precioCompraIndice));

    # Valoracion de Resultado
    print("Porcentaje: " + str(porcentajeGanar));
    ganado = 0
    for i in range(diaCompra,filasColumnas):
        valorEstudiado = matrizIndice[i]
        porcentaje = 1 - (precioCompraIndice/valorEstudiado)
        if (porcentaje>porcentajeGanar):
            print ("Porcentaje Venta: "+str(porcentaje));
            print ("Precio Venta: "+str(valorEstudiado));
            print ("GANAS: SI! en dia "+str(i));
            ganado = ganado + 1

    # Escribimos los resultados
    s = "" + indice +"|" + fechaInicio +"|" + fechaFin +"|" + str(porcentajeGanar) +"|" + str(diaCompra) +"|" + str(precioCompraIndice) +"|" + str(porcentaje) +"|" + str(valorEstudiado) +"|" + str(i) +"|" + str(ganado)
    with open("resultados.txt", "a") as myfile:
        myfile.write(s+"\n")

# Main
with open("indices.txt") as f:
    for line in f:
        indice = line.split()[0]
        valoraInversion(indice,0.07,"01/07/2016","01/09/2016",1,0)
