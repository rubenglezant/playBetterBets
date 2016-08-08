from __future__ import print_function
import pandas as pd
import numpy as np
import argparse
from jinja2 import Environment, FileSystemLoader

# Read in the file and get our pivot table summary
df = pd.read_excel("datos2.xlsx")
df['Benef'] = df['Margen'] * df['PVP']

index_list=["Estado", "Cliente","Resp"]
value_list=["PVP", "Margen"]
# table = pd.pivot_table(df, index=index_list, values=value_list,aggfunc=[np.sum, np.mean], fill_value=0)
table = pd.pivot_table(df, index=index_list, values=value_list,aggfunc=[np.sum], fill_value=0)
print (table)

index_list=["Estado"]
value_list=["PVP", "Margen"]
table = pd.pivot_table(df, index=index_list, values=value_list,aggfunc=[np.sum], fill_value=0)
print (table)

index_list=["Cliente"]
value_list=["PVP" ,"Benef"]
table = pd.pivot_table(df, index=index_list, values=value_list,aggfunc=[np.sum], fill_value=0)
print(table.to_string)
print (table)

