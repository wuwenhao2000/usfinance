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

# SE iau SKYY tlt XSD o vnq SOCL QTUM
stock_list = ['se','iau','ppa','skyy','tlt','xsd','o','vnq','socl','qtum']

# get the stock history from .xlsx file
df_se = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='se',b=time.strftime("%Y%m%d", time.localtime())))
df_iau = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='iau',b=time.strftime("%Y%m%d", time.localtime())))
df_ppa = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='ppa',b=time.strftime("%Y%m%d", time.localtime())))

df_skyy = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='skyy',b=time.strftime("%Y%m%d", time.localtime())))
df_tlt = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='tlt',b=time.strftime("%Y%m%d", time.localtime())))
df_xsd = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='xsd',b=time.strftime("%Y%m%d", time.localtime())))

df_o = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='o',b=time.strftime("%Y%m%d", time.localtime())))
df_vnq = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='vnq',b=time.strftime("%Y%m%d", time.localtime())))

df_socl = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='socl',b=time.strftime("%Y%m%d", time.localtime())))
df_qtum = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='qtum',b=time.strftime("%Y%m%d", time.localtime())))

# get the beginning time_line
df_se = df_se[df_se['Date']>=date]
df_iau = df_iau[df_iau['Date']>=date]
df_ppa = df_ppa[df_ppa['Date']>=date]

df_skyy = df_skyy[df_skyy['Date']>=date]
df_tlt = df_tlt[df_tlt['Date']>=date]
df_xsd = df_xsd[df_xsd['Date']>=date]

df_o = df_o[df_o['Date']>=date]
df_vnq = df_vnq[df_vnq['Date']>=date]

df_socl = df_socl[df_socl['Date']>=date]
df_qtum = df_qtum[df_qtum['Date']>=date]

# set the index of dataframe
df_se.set_index('Date',inplace=True)
df_iau.set_index('Date',inplace=True)
df_ppa.set_index('Date',inplace=True)

df_skyy.set_index('Date',inplace=True)
df_tlt.set_index('Date',inplace=True)
df_xsd.set_index('Date',inplace=True)

df_o.set_index('Date',inplace=True)
df_vnq.set_index('Date',inplace=True)

df_socl.set_index('Date',inplace=True)
df_qtum.set_index('Date',inplace=True)

# concat multi dataframe into a new one
df = pd.concat([df_se,df_iau,df_ppa,df_skyy,df_tlt,df_xsd,df_o,df_vnq,df_socl,df_qtum],axis=1,keys=stock_list)

# set the columns for dataframe
df.columns.names = ['Stock_Name','Stock_INFO']

# print (df.xs(key="Close",level="Stock_INFO",axis=1))

# generate a new dataframe named returns to save the return value
returns = pd.DataFrame()

# get the return of each stock, (Pt - P(t-1))/P(t-1) here the method .pct_change() is used percentage change
for stock in stock_list:
  returns[stock+"_Return"] = df[stock]['Close'].pct_change()
returns = (returns[1:]) # delete the fist row with NaN

# # standard deviation to test the staskyyity, the less the more stable
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

plt.plot(df.index, df.xs(('se','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='se')
plt.plot(df.index, df.xs(('iau','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='iau')
plt.plot(df.index, df.xs(('ppa','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='ppa')

plt.plot(df.index, df.xs(('skyy','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='skyy')
plt.plot(df.index, df.xs(('xsd','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='xsd')
plt.plot(df.index, df.xs(('tlt','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='tlt')

plt.plot(df.index, df.xs(('o','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='o')
plt.plot(df.index, df.xs(('vnq','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='vnq')

plt.plot(df.index, df.xs(('socl','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='socl')
plt.plot(df.index, df.xs(('qtum','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='qtum')

# plt.plot(df.index, df.xs(('VNQ','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='VNQ')

plt.legend()
plt.show()