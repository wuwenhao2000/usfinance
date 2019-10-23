import sys
import os
import json
import time
import pprint
import yfinance as yf
import socket
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
from datetime import timedelta
from datetime import datetime
tss1 = '2013-10-10 23:40:00'

# abc = ['a','b','c']
# for one in abc:
#   str(one) = one+'ccc'
#   print (one)
# dt = datetime.now()
# dt = dt.replace(year=dt.year-3)
# print (dt)
# ss = datetime.datetime.now() - datetime.timedelta(days=1*365)
# print (ss)
now = datetime.now()+ timedelta(days=-365)
print (now.strftime("%Y-%m-%d"))
# print (time.ctime(1567641600)) # earnings
# print (time.ctime(1567641600))
# print (time.ctime(1567641600))
# print (time.strftime("%Y%m%d%H%M%S", time.localtime()))

# print (sys.argv[0].upper())


# one = (sys.argv[1].upper())

# one = (sys.argv[1].upper())
# json_file = "{}_{}.json".format(one,time.strftime("%Y%m%d", time.localtime())) # today's variable file
# target_json = "{}/{}".format(one,json_file) # today's variable file with relative path
# with open(target_json,'r') as load_f: # get the variable from .json file
#   curr_var = json.loads(json.dumps(eval(load_f.read()))) # transfer the variable from string -> json -> dict
# pprint.pprint (curr_var)


# stock = yf.Ticker(one)
# pprint.pprint (stock.financials)
# pprint.pprint (stock.balance_sheet)
# pprint.pprint (stock.cashflow)
# pprint.pprint (stock.options)


# tickers = yf.Tickers('msft aapl goog')
# # ^ returns a named tuple of Ticker objects

# # access each ticker using (example)
# tickers.msft.info
# tickers.aapl.history(period="1mo")
# tickers.goog.actions

# pprint.pprint (stock.info['bookValue'])
# pprint.pprint (stock.info['priceToBook'])
'''
 'dividendDate': 1571097600,
 'earningsTimestamp': 1565049600, 
#  'earningsTimestampEnd': 1572886800,
#  'earningsTimestampStart': 1572361140,
 'exchangeTimezoneShortName': 'EDT',
 'postMarketTime': 1570222788,
 'regularMarketTime': 1570219287,
'''
