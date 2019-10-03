import yfinance as yf
import numpy
import pandas as pd
import pprint
import time
import os
one = 'PVTL' # set the corresponding stock
stock = yf.Ticker(one) 
df = stock.history(period="max") # get the history behavior of the stock
history_file = "{}_{}.xlsx".format(one,time.strftime("%Y%m%d", time.localtime()))
target_file = "{}/{}".format(one,history_file)
if not os.path.exists(one): # check if there is the corresponding directory of the stock
  os.mkdir(one) # if there is NO corresponding directory, then create it
if not os.path.exists(target_file): # check the exist of target file
  df.to_excel(target_file) # if there is NO target file, then create it


df = pd.read_excel(target_file) 
df['trailingPE'] = df['Close']/stock.info['epsTrailingTwelveMonths']
df['PE%'] = (df['trailingPE'] - df['trailingPE'].min())/(df['trailingPE'].max()-df['trailingPE'].min())
df['Regular%'] = (df['Close'] - df['Close'].min())/(df['Close'].max()-df['Close'].min())
# print (df[df['Date']>time.ctime(stock.info['earningsTimestamp'])][['Date','Close','trailingPE','PE%','Regular%']])
print (df[['Date','Close','trailingPE','PE%','Regular%']])




