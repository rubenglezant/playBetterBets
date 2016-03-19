import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

#Parametros
porcentajeGanar = 0.07

A = np.loadtxt('matriz_porcentajes.dat')

print (A.max())
print (A.min())
print (A.mean())

j = 0
gan = 0
for i in A:
	j = j + 1
	if (i.max()>porcentajeGanar):
		print(j, i.max(), i.min())
		gan = gan + 1

print (gan,j,(gan*100/j))

		
