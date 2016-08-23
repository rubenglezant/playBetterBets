import pandas as pd

df = pd.read_csv('wifi_data1.csv', sep='|')

df2 = df.groupby('MAC').min()

print (df2)