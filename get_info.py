import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib
import seaborn
import pprint
import time
import json
import os

one = 'SE' # set the corresponding stock
# variables setting block
history_file = "{}_{}.xlsx".format(one,time.strftime("%Y%m%d", time.localtime())) # today's history file
target_file = "{}/{}".format(one,history_file) # today's history file with relative path
json_file = "{}_{}.json".format(one,time.strftime("%Y%m%d", time.localtime())) # today's variable file
target_json = "{}/{}".format(one,json_file) # today's variable file with relative path

# get stock information block
if not os.path.exists(one): # check if the corresponding directory exists
  os.mkdir(one) # if there is NO corresponding directory, then create it
if not os.path.exists(target_json): # check if the variable file exists
  stock = yf.Ticker(one) # call yf API
  with open(target_json,'w') as f: # create json file
    f.write(str(stock.info)) # save the stock.info as the json file
    df = stock.history(period="max") # get the history behavior of the stock
    df.to_excel(target_file) # save the stock history behavior as Excel file

# read the local files block
df = pd.read_excel(target_file) # get the stock history from .xlsx file
with open(target_json,'r') as load_f: # get the variable from .json file
  curr_var = json.loads(json.dumps(eval(load_f.read()))) # transfer the variable string -> json -> dict

# data analysis block
# df['eps'] = stock.info['epsTrailingTwelveMonths']
df['eps'] = curr_var['epsTrailingTwelveMonths'] # get the EPS
df['trailingPE'] = df['Close']/df['eps'] # calculate new column "trailingPE = Close/eps"
df['PE%'] = (df['trailingPE'] - df['trailingPE'].min())/(df['trailingPE'].max()-df['trailingPE'].min()) # calculate PE%
df['Regular%'] = (df['Close'] - df['Close'].min())/(df['Close'].max()-df['Close'].min()) # calculate Regular%
# print (df[df['Date']>time.ctime(stock.info['earningsTimestamp'])][['Date','Close','eps','trailingPE','PE%','Regular%',]])
print (df[['Date','Close','trailingPE','PE%','Regular%']])