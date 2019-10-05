import yfinance as yf
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import pprint
import time
import json
import os
import sys

# get the corresponding stock from input
one = sys.argv[1].upper()

# variables setting block
history_file = "{}_{}.xlsx".format(one,time.strftime("%Y%m%d", time.localtime())) # today's history file
target_file = "{}/{}".format(one,history_file) # today's history file with relative path
json_file = "{}_{}.json".format(one,time.strftime("%Y%m%d", time.localtime())) # today's variable file
target_json = "{}/{}".format(one,json_file) # today's variable file with relative path

# get stock information block
if not os.path.exists(one): # check if the corresponding directory exists
  os.mkdir(one) # if there is NO corresponding directory, then create it
if not os.path.exists(target_json): # check if the variable file exists
  stock = yf.Ticker(one) # call yf API to get the data
  with open(target_json,'w') as f: # create json file
    f.write(str(stock.info)) # save the stock.info as the json file
  df = stock.history(period="max") # get the history behavior of the stock
  df.to_excel(target_file) # save the stock history behavior as Excel file

# read the local files block
df = pd.read_excel(target_file) # get the stock history from .xlsx file
with open(target_json,'r') as load_f: # get the variable from .json file
  curr_var = json.loads(json.dumps(eval(load_f.read()))) # transfer the variable from string -> json -> dict

# data analysis block
# df['eps'] = stock.info['epsTrailingTwelveMonths']
df['book'] = curr_var['bookValue'] # get the book value
df['PB'] = df['Close']/df['book'] # calculate new column "trailingPB = Close/book"
df['PB%'] = (df['PB'] - df['PB'].min())/(df['PB'].max()-df['PB'].min())*(100) # calculate PB%
df['Regular%'] = (df['Close'] - df['Close'].min())/(df['Close'].max()-df['Close'].min())*(100) # calculate Regular%
df['Rollback%'] = (df['Close'].max() - df['Close'])/df['Close'].max()*(100) # calculate Regular%

if int(curr_var['epsTrailingTwelveMonths'])>0: # when eps is grater than 0
  df['eps'] = curr_var['epsTrailingTwelveMonths'] # get the eps
  df['PE'] = df['Close']/df['eps'] # calculate new column "PE = Close/eps"
  df['PE%'] = (df['PE'] - df['PE'].min())/(df['PE'].max()-df['PE'].min())*(100) # calculate PE%
  df=df[['Date','Close','PB','PB%','PE','PE%','Rollback%']] # get the result of all history
else: # when eps is less than 0
  df=df[['Date','Close','PB','PB%','Rollback%']] # get the result of all history

# print (df[>time.ctime(curr_var['earningsTimestamp'])][['Date','Close','eps','trailingPE','PE%','Regular%',]]) # get the result from earningsTimestamp
# print (df[['Date','Close','trailingPB','trailingPE','PE%','PB%','Regular%']]) # get the result of all history
# print (df[df['Close'] == df['Close'].max()])


# create the coordinate based on above data
if sys.argv[2].upper()=='Y':
  x = df['Date'] # set x axis variable
  y = df['PB%'] # set y axis variable
  plt.title("PB% vs Time") # set picture title
  plt.xlabel("Time") # set x axis label
  plt.ylabel("PB") # set y axis label
  plt.plot(x,y) # create the coordinate
  plt.show() # show the coordinate

else:
  print (df)

# sns.set_style("whitegrid")  
# plt.plot(np.arange(10))  
# plt.show()