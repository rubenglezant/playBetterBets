import pandas.io.data as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import sys

#Parametros
indice = "GAM.MC"
porcentajeGanar = 0.087
criterio = 1;
# 0 - Ningun Criterio
# 1 - Tres subidas consecutivas

# Recogemos los valores del indice para el test
start = datetime.datetime(2016, 1, 1)
end = datetime.datetime(2016, 3, 24)
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
    precioCompraIndice = 15.820

print("Dia Compra: " + str(i+2));
print("Precio Compra: " + str(precioCompraIndice));

# Valoracion de Resultado
print("Porcentaje: " + str(porcentajeGanar));
for i in range(0,filasColumnas):
    valorEstudiado = matrizIndice[i]
    porcentaje = 1 - (precioCompraIndice/valorEstudiado)
    if (porcentaje>porcentajeGanar):
        print ("Porcentaje Venta: "+str(porcentaje));
        print ("Precio Venta: "+str(valorEstudiado));
        print ("GANAS: SI! en dia "+str(i));
        break;
