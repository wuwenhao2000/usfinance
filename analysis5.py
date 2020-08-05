import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pprint
import time
import json
import os
import sys
from pandas_datareader import data,wb
from datetime import timedelta
from datetime import datetime
# import datetime

# beginning date of stock dataframe analysis
date = '2019-01-01'

stock_list = ['ftxl','usd','xsd','soxx']

# get the stock history from .xlsx file
df_ftxl = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='ftxl',b=time.strftime("%Y%m%d", time.localtime())))
df_usd = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='usd',b=time.strftime("%Y%m%d", time.localtime())))
df_xsd = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='xsd',b=time.strftime("%Y%m%d", time.localtime())))
df_soxx = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='soxx',b=time.strftime("%Y%m%d", time.localtime())))

# get the beginning time_line
df_ftxl = df_ftxl[df_ftxl['Date']>=date]
df_usd = df_usd[df_usd['Date']>=date]
df_xsd = df_xsd[df_xsd['Date']>=date]
df_soxx = df_soxx[df_soxx['Date']>=date]

# set the index of dataframe
df_ftxl.set_index('Date',inplace=True)
df_usd.set_index('Date',inplace=True)
df_xsd.set_index('Date',inplace=True)
df_soxx.set_index('Date',inplace=True)

# concat multi dataframe into a new one
df = pd.concat([df_ftxl,df_usd,df_xsd,df_soxx],axis=1,keys=stock_list)

# set the columns for dataframe
df.columns.names = ['Stock_Name','Stock_INFO']

# print (df.xs(key="Close",level="Stock_INFO",axis=1))

# generate a new dataframe named returns to save the return value
returns = pd.DataFrame()

# get the return of each stock, (Pt - P(t-1))/P(t-1) here the method .pct_change() is used percentage change
for stock in stock_list:
  returns[stock+"_Return"] = df[stock]['Close'].pct_change()
returns = (returns[1:]) # delete the fist row with NaN

# # standard deviation to test the stability, the less the more stable
# print (returns.std()) 

# # get the standard deviation of specific period
# print (returns.loc['2019-01-01':].std()) 

# # the density distribution of the return
# sns.distplot(returns['o_Return'],color='green',bins=220) 

# # the historical Close price of stocks involved
# df.xs(key="Close",axis=1,level='Stock_INFO').plot() 

# # the grab method of multi index dataframe
# print (df.xs(('o','Close'),axis=1,level=('Stock_Name','Stock_INFO')))

# # show the correlationship of the value of different columns
# sns.pairplot(returns,diag_kind="kde", markers="+")
# sns.pairplot(returns)

# # heatmap and clustermap must be corr() model
# sns.heatmap(df.xs(key="Close",axis=1,level='Stock_INFO').corr())
# sns.clustermap(df.xs(key="Close",axis=1,level='Stock_INFO').corr(),annot=True)


# # window=30 the avg value of the Close 
# plt.plot(df.index, df.xs(('ftxl','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='ftxl AVG')
# plt.plot(df.index, df.xs(('usd','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='usd AVG')
# plt.plot(df.index, df.xs(('xsd','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='xsd AVG')
# plt.plot(df.index, df.xs(('soxx','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='soxx AVG')

plt.plot(df.index, df.xs(('ftxl','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='ftxl')
plt.plot(df.index, df.xs(('usd','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='usd')
plt.plot(df.index, df.xs(('xsd','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='xsd')
plt.plot(df.index, df.xs(('soxx','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='soxx')

plt.legend()
plt.show()