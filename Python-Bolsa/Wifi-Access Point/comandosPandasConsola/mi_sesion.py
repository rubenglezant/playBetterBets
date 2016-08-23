# coding: utf-8
import pandas as pd
df.read_csv('wifi_20160822_0304.txt', sep="|")
df = pd.read_csv('wifi_20160822_0304.txt', sep="|")
df = pd.read_csv('wifi_20160822_0304.txt', sep="|")
df.groupby('MAC')
df2=df.groupby('MAC')
df2.agg('count')
df2.agg('min')
df.head()
df2 = df.drop('MACDst',axis=1)
df2 = df2.drop('Signal',axis=1)
df2 = df2.drop('Num2',axis=1)
df2 = df2.drop('Num',axis=1)
df2 = df2.drop('Channel',axis=1)
df3 = df2.groupby('MAC').agg('min')
df3
df3['Min'] = df3['Seg']
df4 = df2.groupby('MAC').agg('max')
df4
df3['Max'] = df3['Seg']
df3
df3['Max'] = df4['Seg']
df3
df3['Seg'] = df3['Max']-df3['Min']
df3
df3.sort('Seg')
df2=df.groupby('MAC').agg('Min')
df2=df.groupby('MAC').agg('min')
df2.head
dfFin = df3
dfFin['Signal'] = df2['Num2']
dfFin
dfFin.sort('Signal')
dfFin['Hours'] = df['Seg']/3600
dfFin
df.to_numeric('Seg')
df['Seg'].apply(pd.to_numeric)
df['Seg'].apply(pd.to_numeric, errors='ignore')
df = pd.read_csv('wifi_20160822_0304.txt', sep="|", dtype={'Seg': numpy.float32})
import numpy
df = pd.read_csv('wifi_20160822_0304.txt', sep="|", dtype={'Seg': numpy.float32})
get_ipython().magic('save mi_sesion')
