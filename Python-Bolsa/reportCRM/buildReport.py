import urllib3
import urllib.request
import base64
import json
import pandas as pd
from tabulate import tabulate
import codecs
import numpy as np

url = 'https://infeci.capsulecrm.com/api/opportunity'

headers = {}
# base64string = base64.urlsafe_b64encode('2d486e42771eee18125b8aef3afe216d:4c2TNRdi')
base64string = base64.encodestring(('2d486e42771eee18125b8aef3afe216d:4c2TNRdi').encode()).decode().replace('\n', '')
headers['Authorization'] = "Basic %s" % base64string
headers['Accept'] = "application/json"
req = urllib.request.Request(url, headers = headers)
resp = urllib.request.urlopen(req)
reader = codecs.getreader("utf-8")
data = json.load(reader(resp))
print (data)

# Creamos el CSV con las oportunidades
# atributos = ['name','probability','expectedCloseDate','createdOn','updatedOn','value','currency','partyId','milestoneId','milestone','owner','id','durationBasis']
# s = ""
# for atr in atributos:
#     s = s + atr + ","
# s = s + "\n"
# for op in data['opportunities']['opportunity']:
#     for atr in atributos:
#         s = s + op[atr] + ","
#     s = s + "\n"
#
# text_file = open("oportunidades.csv", "w")
# text_file.write(s)
# text_file.close()

data = pd.read_csv('oportunidades.csv')
print (tabulate(data, headers='keys', tablefmt='psql'))

# 1- Estado de lo presentado
# http://pbpython.com/pandas-pivot-table-explained.html
print ("\tESTADO GLOBAL DE LAS OPORTUNIDADES")
data = pd.read_csv('oportunidades.csv')
df = data
df = df.drop(df.columns[[0, 1, 2, 3, 4, 6, 7, 8, 10, 11, 12]], axis=1)
df['benef'] = df['value'] * df['margen'] / 100
pt = df.groupby(['milestone']).sum()
pt['margen'] = 100 * pt ['benef'] / pt['value']
print (tabulate(pt, headers='keys', tablefmt='psql'))
print ("\tValor Total: %s" % data['value'].sum())


# 1- Estado de lo presentado
# http://pbpython.com/pandas-pivot-table-explained.html
print ("\n\n")
print ("\tPROXIMAS OFERTAS A PRESENTAR")
data = pd.read_csv('oportunidades.csv')
df = data
df['benef'] = df['value'] * df['margen'] / 100
df =  (df[df['milestone']=='New'])
df = df.sort_values('expectedCloseDate')
df = df.drop(df.columns[[1, 3, 4, 6, 7, 8, 10, 11, 12,13,14]], axis=1)
print (tabulate(df, headers='keys', tablefmt='psql'))

# 1- Estado de lo presentado
# http://pbpython.com/pandas-pivot-table-explained.html
print ("\n\n")
print ("\tANALIZANDO...")
data = pd.read_csv('oportunidades.csv')
df = data
df['benef'] = df['value'] * df['margen'] / 100
df =  (df[df['milestone']=='New'])
df = df.sort_values('expectedCloseDate')
print (df)
df = df.drop(df.columns[[1, 3, 4, 6, 7, 8, 10, 11, 12,13,14]], axis=1)
print (tabulate(df, headers='keys', tablefmt='psql'))

# {u'name': u'Definici\xf3n de Tarjeta de Transporte', u'probability': u'10', u'expectedCloseDate': u'2016-09-15T00:00:00Z',
    # u'createdOn': u'2016-08-17T09:48:26Z', u'updatedOn': u'2016-08-17T11:29:53Z', u'value': u'95000.00', u'currency': u'EUR',
    # u'partyId': u'115869164', u'milestoneId': u'405855', u'milestone': u'New', u'owner': u'rubenglezant', u'id': u'4609271',
    # u'durationBasis': u'FIXED'}

# response = urllib2.urlopen('https://api.instagram.com/v1/tags/pizza/media/XXXXXX')

# curl -u 2d486e42771eee18125b8aef3afe216d:4c2TNRdi https://infeci.capsulecrm.com/api/party