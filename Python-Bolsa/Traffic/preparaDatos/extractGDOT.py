import pandas as pd
import numpy as np
import csv as csv
from sklearn.ensemble import RandomForestClassifier

# CON ESTO GENERAMOS EL VECTOR DE GDTO
# HAY QUE GENERAR el FICHERO

data = pd.read_csv("./gdot_35418_2016_4.csv")

np = (data.values)

filas,cols = (np.shape)

print ("Dia,Hora,Valor")
for i in range(0,filas):
    for j in range(2,cols-1):
        print (str(np[i][0])[-2:] + "," + str(j-2) + "," + str(np[i][j]))


