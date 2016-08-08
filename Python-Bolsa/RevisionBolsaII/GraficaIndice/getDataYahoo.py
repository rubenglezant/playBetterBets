import pandas.io.data as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import sys
import pandas as pd

#Parametros
accederWeb = True
indice = "GAM.MC"

# Recogemos el valor de los datos de Web
if (accederWeb):
    start = datetime.datetime(2015, 1, 1)
    end = datetime.datetime(2016, 8, 8)
    f = web.DataReader(indice, 'yahoo', start, end)
    f = (f["Close"])
    f.to_csv('out.csv')

# Dibujamos el valor durante el periodo
fedata = pd.read_csv('out.csv', index_col=0)
print (fedata)
fedata.plot(kind='line')
plt.title(indice)
#plt.show()
plt.savefig(indice+".jpg")




