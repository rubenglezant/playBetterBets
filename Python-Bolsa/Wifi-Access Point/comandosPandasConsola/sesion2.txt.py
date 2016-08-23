# coding: utf-8
import pandas as pd
import numpy
df = pd.read_csv('wifi_20160823_0200_new2.txt', sep="|", dtype={'Seg': numpy.float32})
df2 = df.drop('MACDst',axis=1)
df2 = df2.drop('Signal2',axis=1)
df2 = df2.drop('Num2',axis=1)
df2 = df2.drop('Num',axis=1)
df2 = df2.drop('Channel',axis=1)
df2
df3 = df2[df2['MAC'=='d8:b6:b7:0d:48:7e']
]
df2[df2['MAC'=='d8:b6:b7:0d:48:7e']]
df2.head
df2['MAC'=='d8:b6:b7:0d:48:7e']
df2['MAC']
df2['MAC'=='d8:b6:b7:0d:48:7e']
df2
df2.groupby('MAC').agg('min')
df3 = df2.groupby('MAC').agg('min')
df3[df3['MAC']=='d8:b6:b7:0d:48:7e']
df3[df3['MAC'=='d8:b6:b7:0d:48:7e']]
df3[df3['MAC']=='d8:b6:b7:0d:48:7e']
df3
df3['MAC'=='d8:b6:b7:0d:48:7e']
df3
df3.sort('Signal')
df3.to_csv('salida.csv')
df3 = df2.groupby('MAC').agg('max')
df3.to_csv('salida.csv')
df3.sort('Seg')
df3.sort('Signal')
df4 = df2.groupby('MAC').agg('min')
dfFin = df3
dfFin['minSignal'] = df4['Signal']
dfFin['minSeg'] = df4['Seg']
dfFin.to_csv('salida.csv')
dfFin['totalSeg'] = dfFin['Seg']-dfFin['minSeg']
dfFin.sort('totalSeg')
dfFin.sort('totalSeg').to_csv('resultados.csv')
