import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

f = pd.read_csv('gas.mc.csv')

print (f[:2])

r = f[['Open']]

filasColumnas = r.index.max() + 1
matrizPorcentajes = np.empty([filasColumnas,filasColumnas],dtype='double')

for i in r.index:
	valorEstudiado = r.ix[i]
	for j in r.index:
		if (j<i):
			matrizPorcentajes[i,j] = 0
		else:
			matrizPorcentajes[i,j] = ((r.ix[j]-valorEstudiado)/valorEstudiado)
			

np.savetxt('matriz_porcentajes.dat', matrizPorcentajes, fmt='%.4e')
