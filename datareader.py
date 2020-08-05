import pandas_datareader.data as web
import datetime
import os
import pandas_datareader as pdr


symbol = 'WIKI/AAPL'  # or 'AAPL.US'

df = web.DataReader(symbol, 'quandl', '2015-01-01', '2015-01-05')

print(df)