import pandas as pd
import numpy as np
import csv as csv
from sklearn.ensemble import RandomForestClassifier

# CON ESTO GENERAMOS EL VECTOR DE BING
# HAY QUE GENERAR el FICHERO

df = pd.read_csv("./trafico-DATA-GDOT2.csv", sep=';')

df = df.sort_index(by=['Fecha Hora'], ascending=[True])

# print (df)

print ("Dia,Hora,ValorMedio,Indice,Valor")
horaAnterior = 0
valorMedio = 0
indiceMedio = 0
for index, row in df.iterrows():
    fechahora = row['Fecha Hora']
    dia = (int)((fechahora-5000000)/10000)
    hora = (int)((fechahora-5000000-dia*10000)/100)
    valor = row['Valor Estimado']
    # print (str(dia) + " " + str(hora) + " " + str(valor))
    if (hora == horaAnterior):
        valorMedio = valor + valorMedio;
        indiceMedio = indiceMedio + 1
    else:
        valor = 0
        if (indiceMedio>0):
            valor = valorMedio/indiceMedio;
        print (str(dia) + "," + str(hora) + "," + str(valorMedio)+ "," + str(indiceMedio)+ "," + str(valor))
        horaAnterior = hora;




