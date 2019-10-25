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
date = '2010-01-01'


stock_list = ['ivv','voo','spy']

# get the stock history from .xlsx file
df_ivv = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='ivv',b=time.strftime("%Y%m%d", time.localtime())))
df_voo = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='voo',b=time.strftime("%Y%m%d", time.localtime())))
df_spy = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='spy',b=time.strftime("%Y%m%d", time.localtime())))

# get the beginning time_line
df_ivv = df_ivv[df_ivv['Date']>=date]
df_voo = df_voo[df_voo['Date']>=date]
df_spy = df_spy[df_spy['Date']>=date]

# set the index of dataframe
df_ivv.set_index('Date',inplace=True)
df_voo.set_index('Date',inplace=True)
df_spy.set_index('Date',inplace=True)

# concat multi dataframe into a new one
df = pd.concat([df_ivv,df_voo,df_spy],axis=1,keys=stock_list)

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
# plt.plot(df.index, df.xs(('O','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='o AVG')
# plt.plot(df.index, df.xs(('BXP','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='bxp AVG')
# plt.plot(df.index, df.xs(('spy','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='spy AVG')
# plt.plot(df.index, df.xs(('VNQ','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='vnq AVG')

plt.plot(df.index, df.xs(('ivv','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='ivv')
plt.plot(df.index, df.xs(('voo','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='voo')
plt.plot(df.index, df.xs(('spy','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='spy')
# plt.plot(df.index, df.xs(('VNQ','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='VNQ')

plt.legend()
plt.show()