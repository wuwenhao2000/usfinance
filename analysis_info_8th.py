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


stock_list = ['scho','vgsh','shv','bil','shy','near']

# get the stock history from .xlsx file
df_scho = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='scho',b=time.strftime("%Y%m%d", time.localtime())))
df_vgsh = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='vgsh',b=time.strftime("%Y%m%d", time.localtime())))
df_shv = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='shv',b=time.strftime("%Y%m%d", time.localtime())))

df_bil = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='bil',b=time.strftime("%Y%m%d", time.localtime())))
df_shy = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='shy',b=time.strftime("%Y%m%d", time.localtime())))
df_near = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='near',b=time.strftime("%Y%m%d", time.localtime())))

# get the beginning time_line
df_scho = df_scho[df_scho['Date']>=date]
df_vgsh = df_vgsh[df_vgsh['Date']>=date]
df_shv = df_shv[df_shv['Date']>=date]

df_bil = df_bil[df_bil['Date']>=date]
df_shy = df_shy[df_shy['Date']>=date]
df_near = df_near[df_near['Date']>=date]

# set the index of dataframe
df_scho.set_index('Date',inplace=True)
df_vgsh.set_index('Date',inplace=True)
df_shv.set_index('Date',inplace=True)

df_bil.set_index('Date',inplace=True)
df_shy.set_index('Date',inplace=True)
df_near.set_index('Date',inplace=True)

# concat multi dataframe into a new one
df = pd.concat([df_scho,df_vgsh,df_shv,df_bil,df_shy,df_near],axis=1,keys=stock_list)

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
# plt.plot(df.index, df.xs(('shv','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='shv AVG')
# plt.plot(df.index, df.xs(('VNQ','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='vnq AVG')

plt.plot(df.index, df.xs(('scho','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='scho')
plt.plot(df.index, df.xs(('vgsh','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='vgsh')
plt.plot(df.index, df.xs(('shv','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='shv')

plt.plot(df.index, df.xs(('bil','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='bil')
plt.plot(df.index, df.xs(('shy','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='shy')
plt.plot(df.index, df.xs(('near','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='near')


# plt.plot(df.index, df.xs(('VNQ','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='VNQ')

plt.legend()
plt.show()