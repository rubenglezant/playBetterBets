import pandas as pd
from pandas import DataFrame
from scipy.stats.stats import pearsonr
import numpy as np
from scipy.stats import linregress
import matplotlib.pyplot as plt

# Recuperamos los valores de la Web de GDOT
df = pd.read_csv('bindGDOT.csv')
npGDOT = df['Valor']

# Recuperamos los valores de BING
df = pd.read_csv("./trafico-DATA-GDOT2.csv", sep=';')
df = df.sort_index(by=['Fecha Hora'], ascending=[True])
horaAnterior = 0
valorMedio = 0
indiceMedio = 0
npValores = []
npBING = []
for index, row in df.iterrows():
    fechahora = row['Fecha Hora']
    dia = (int)((fechahora-5000000)/10000)
    hora = (int)((fechahora-5000000-dia*10000)/100)
    valor = row['Valor Estimado']
    # print (str(dia) + " " + str(hora) + " " + str(valor))
    if (hora == horaAnterior):
        valorMedio = valor + valorMedio;
        indiceMedio = indiceMedio + 1
        npValores.append(valor)
    else:
        valor = 0
        if (indiceMedio>0):
            valor = np.mean(npValores) - 90
        if ((dia >=16) and (dia <=17) ):
            npBING.append(valor)
        horaAnterior = hora;
        indiceMedio = 0;
        valorMedio = 0;
        npValores = [];

# Debemos realizar el ajuste horario. 6 horas menos en USA
horasDiferencia = 6
npGDOT = npGDOT[:horasDiferencia*(-1)]
npBING = npBING[horasDiferencia:]

print pearsonr(npGDOT,npBING)

a = linregress(npGDOT,npBING)
print (a)

#plt.scatter(npBING,npGDOT,alpha=0.5)
plt.figure(1)
width = .35
ind = np.arange(len(npBING))
plt.bar(ind, npBING, width=width)
plt.figure(2)
width = .35
ind = np.arange(len(npGDOT))
plt.bar(ind, npGDOT, width=width)
plt.show()



