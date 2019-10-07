import sys
import os
import json
import time
import pprint
import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
# abc = {1:'abc',2:'def'}
# print (abc[1])
# import time
# print (time.ctime(1567641600)) # earnings
# print (time.ctime(1567641600))
# print (time.ctime(1567641600))
# print (time.strftime("%Y%m%d%H%M%S", time.localtime()))

# print (sys.argv[0].upper())

# one = (sys.argv[1].upper())
# json_file = "{}_{}.json".format(one,time.strftime("%Y%m%d", time.localtime())) # today's variable file
# target_json = "{}/{}".format(one,json_file) # today's variable file with relative path
# with open(target_json,'r') as load_f: # get the variable from .json file
#   curr_var = json.loads(json.dumps(eval(load_f.read()))) # transfer the variable from string -> json -> dict
# pprint.pprint (curr_var)


# stock = yf.Ticker(one)
# pprint.pprint (stock.info['regularMarketPrice'])

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

# fig = plt.figure(num=1, figsize=(15, 8),dpi=80) 
fig = plt.figure()

plt.plot(np.arange(0,1,0.1),range(0,10,1),label='abc',color='green',lw=1,ls='-.')
plt.plot(np.arange(0,1,0.1),range(0,20,2),label='def',color='purple',lw=3,ls='--')
plt.title("PB% vs Time")
plt.xlabel("Time")
plt.ylabel("Value")
plt.legend()
plt.show()
