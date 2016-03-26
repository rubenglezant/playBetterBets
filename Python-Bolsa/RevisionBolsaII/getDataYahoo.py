import pandas.io.data as web
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import sys

start = datetime.datetime(2015, 1, 1)
end = datetime.datetime(2016, 3, 24)

f = web.DataReader("GAM.MC", 'yahoo', start, end)

f = (f["Close"])

f.to_csv('out.csv')



