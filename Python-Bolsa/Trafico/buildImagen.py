import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import cm

# matplotlib.style.use('ggplot')

fig, ax = plt.subplots()

df = pd.read_csv('data.csv', index_col=[0], skipinitialspace=True, sep=';')
df = df.drop('distancia', 1)
#df = df.drop('Valor Minimo', 1)
df = df.sort(ascending=[1])
print df

# df.plot(kind='bar');
#df.plot(kind='bar',alpha=0.75, rot=0)
#df.plot(kind='bar',alpha=0.75, rot=0, fontsize=7)

#plt.xticks(df.index, df.index, rotation=90)

valor = df['Valor Estimado'].values
valorFijo = df['Valor Minimo'].values

plt.setp(ax.get_xticklabels(), visible=False)
plt.grid(True)
plt.title("Analisis de Trafico")
plt.xlabel("Periodo "+str(df.index.min())+ " - " +str(df.index.max()))
plt.ylabel("Tiempo en Segundos")

plt.plot(valor)
plt.plot(valorFijo)

#df.plot(kind='bar',legend=False, fontsize=7, title='TEST');

plt.savefig('trafico.png')
