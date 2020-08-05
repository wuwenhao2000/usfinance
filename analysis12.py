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


stock_list = ['ita','xar','ppa','dfen','ifly','fite','ufo','rokt']

# get the stock history from .xlsx file
df_ita = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='ita',b=time.strftime("%Y%m%d", time.localtime())))
df_xar = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='xar',b=time.strftime("%Y%m%d", time.localtime())))
df_ppa = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='ppa',b=time.strftime("%Y%m%d", time.localtime())))

df_dfen = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='dfen',b=time.strftime("%Y%m%d", time.localtime())))
df_ifly = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='ifly',b=time.strftime("%Y%m%d", time.localtime())))
df_fite = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='fite',b=time.strftime("%Y%m%d", time.localtime())))

df_ufo = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='ufo',b=time.strftime("%Y%m%d", time.localtime())))
df_rokt = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='rokt',b=time.strftime("%Y%m%d", time.localtime())))

# get the beginning time_line
df_ita = df_ita[df_ita['Date']>=date]
df_xar = df_xar[df_xar['Date']>=date]
df_ppa = df_ppa[df_ppa['Date']>=date]

df_dfen = df_dfen[df_dfen['Date']>=date]
df_ifly = df_ifly[df_ifly['Date']>=date]
df_fite = df_fite[df_fite['Date']>=date]

df_ufo = df_ufo[df_ufo['Date']>=date]
df_rokt = df_rokt[df_rokt['Date']>=date]

# set the index of dataframe
df_ita.set_index('Date',inplace=True)
df_xar.set_index('Date',inplace=True)
df_ppa.set_index('Date',inplace=True)

df_dfen.set_index('Date',inplace=True)
df_ifly.set_index('Date',inplace=True)
df_fite.set_index('Date',inplace=True)

df_ufo.set_index('Date',inplace=True)
df_rokt.set_index('Date',inplace=True)

# concat multi dataframe into a new one
df = pd.concat([df_ita,df_xar,df_ppa,df_dfen,df_ifly,df_fite,df_ufo,df_rokt],axis=1,keys=stock_list)

# set the columns for dataframe
df.columns.names = ['Stock_Name','Stock_INFO']

# print (df.xs(key="Close",level="Stock_INFO",axis=1))

# generate a new dataframe named returns to save the return value
returns = pd.DataFrame()

# get the return of each stock, (Pt - P(t-1))/P(t-1) here the method .pct_change() is used percentage change
for stock in stock_list:
  returns[stock+"_Return"] = df[stock]['Close'].pct_change()
returns = (returns[1:]) # delete the fist row with NaN

# # standard deviation to test the stadfenity, the less the more stable
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
# plt.plot(df.index, df.xs(('ppa','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='ppa AVG')
# plt.plot(df.index, df.xs(('VNQ','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='vnq AVG')

plt.plot(df.index, df.xs(('ita','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='ita')
plt.plot(df.index, df.xs(('xar','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='xar')
plt.plot(df.index, df.xs(('ppa','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='ppa')

plt.plot(df.index, df.xs(('dfen','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='dfen')
plt.plot(df.index, df.xs(('fite','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='fite')
plt.plot(df.index, df.xs(('ifly','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='ifly')

plt.plot(df.index, df.xs(('ufo','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='ufo')
plt.plot(df.index, df.xs(('rokt','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='rokt')

# plt.plot(df.index, df.xs(('VNQ','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='VNQ')

plt.legend()
plt.show()