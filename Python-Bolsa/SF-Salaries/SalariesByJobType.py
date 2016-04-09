import pandas as pd
import numpy as np

df = pd.read_csv('./output/Salaries.csv')
# Quitamos los Nan
df.fillna('', inplace=True)

totalregs, columns = (df.shape)

print (totalregs)

#df = df[:100]

print (df.head)

# Disticnt features
listFeatures = ['Year','JobTitle','Agency','Status']
for i in listFeatures:
    listJobs = np.unique(df[i])
    print ("Distinct "+i)
    print (listJobs.shape[0])

for i in listJobs:
    rows = df.loc[df['JobTitle'] == i]
    #print(str(rows['TotalPay'].mean(axis=0)) + "\t" + i)
    #print (i)

