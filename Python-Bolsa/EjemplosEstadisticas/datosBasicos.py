import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # importando matplotlib
import seaborn as sns # importando seaborn
from scipy import stats # importando scipy.stats

np.random.seed(2131982) # para poder replicar el random
datos = np.random.randn(5, 4) # datos normalmente distribuidos

# media aritmetica
datos.mean() # Calcula la media aritmetica de
np.mean(datos) # Mismo resultado desde la funcion de numpy
datos.mean(axis=1) # media aritmetica de cada fila
datos.mean(axis=0) # media aritmetica de cada columna
# mediana
np.median(datos)
np.median(datos, 0) # media aritmetica de cada columna
 # Desviacion tipica
np.std(datos)
np.std(datos, 0) # Desviacion tipica de cada columna
# varianza
np.var(datos)
np.var(datos, 0) # varianza de cada columna
# el 2do array devuelve la frecuencia.
datos2 = np.array([1, 2, 3, 6, 6, 1, 2, 4, 2, 2, 6, 6, 8, 10, 6])
# correlacion
print (np.corrcoef(datos)) # Crea matriz de correlacion.
# calculando la correlacion entre dos vectores.
np.corrcoef(datos[0], datos[1])
# covarianza
np.cov(datos) # calcula matriz de covarianza
# covarianza de dos vectores
np.cov(datos[0], datos[1])

print (stats.mode(datos))

# parametros esteticos de seaborn
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize": (8, 4)})
