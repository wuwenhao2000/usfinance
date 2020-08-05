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


stock_list = ['ibuy','ebiz','onln','socl','clix','emqq','sgol','botz','clou']

# get the stock history from .xlsx file
df_ibuy = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='ibuy',b=time.strftime("%Y%m%d", time.localtime())))
df_ebiz = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='ebiz',b=time.strftime("%Y%m%d", time.localtime())))
df_onln = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='onln',b=time.strftime("%Y%m%d", time.localtime())))
df_socl = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='socl',b=time.strftime("%Y%m%d", time.localtime())))
df_clix = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='clix',b=time.strftime("%Y%m%d", time.localtime())))
df_emqq = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='emqq',b=time.strftime("%Y%m%d", time.localtime())))
df_sgol = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='sgol',b=time.strftime("%Y%m%d", time.localtime())))
df_botz = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='botz',b=time.strftime("%Y%m%d", time.localtime())))
df_clou = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='clou',b=time.strftime("%Y%m%d", time.localtime())))


# get the beginning time_line  ['ibuy','ebiz','onln','socl','clix','o','se','emqq','sgol','botz','clou','vt','xsd','soxx','socl','ign']
df_ibuy = df_ibuy[df_ibuy['Date']>=date]
df_ebiz = df_ebiz[df_ebiz['Date']>=date]
df_onln = df_onln[df_onln['Date']>=date]
df_socl = df_socl[df_socl['Date']>=date]
df_clix = df_clix[df_clix['Date']>=date]
df_emqq = df_emqq[df_emqq['Date']>=date]
df_sgol = df_sgol[df_sgol['Date']>=date]
df_botz = df_botz[df_botz['Date']>=date]
df_clou = df_clou[df_clou['Date']>=date]


# set the index of dataframe ['ibuy','ebiz','onln','socl','clix','o','se','emqq','sgol','botz','clou','vt','xsd','soxx','socl','ign']
df_ibuy.set_index('Date',inplace=True)
df_ebiz.set_index('Date',inplace=True)
df_onln.set_index('Date',inplace=True)
df_socl.set_index('Date',inplace=True)
df_clix.set_index('Date',inplace=True)
df_emqq.set_index('Date',inplace=True)
df_sgol.set_index('Date',inplace=True)
df_botz.set_index('Date',inplace=True)
df_clou.set_index('Date',inplace=True)

# concat multi dataframe into a new one ['ibuy','ebiz','onln','socl','clix','o','se','emqq','sgol','botz','clou','vt','xsd','soxx','socl','ign']
df = pd.concat([df_ibuy,df_ebiz,df_onln,df_socl,df_clix,df_emqq,df_sgol,df_botz,df_clou],axis=1,keys=stock_list)

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




# # ['ibuy','ebiz','onln','socl','clix','o','se','emqq','sgol','botz','clou','vt','xsd','soxx','socl','ign']
# plt.plot(df.index, df.xs(('ibuy','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='ibuy')
# plt.plot(df.index, df.xs(('ebiz','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='ebiz')
# plt.plot(df.index, df.xs(('onln','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='onln')
# plt.plot(df.index, df.xs(('socl','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='socl')
# plt.plot(df.index, df.xs(('clix','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='clix')
# plt.plot(df.index, df.xs(('o','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='o')
# # plt.plot(df.index, df.xs(('se','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='se')
# plt.plot(df.index, df.xs(('emqq','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='emqq')
# plt.plot(df.index, df.xs(('sgol','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='sgol')
# plt.plot(df.index, df.xs(('botz','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='botz')
# plt.plot(df.index, df.xs(('clou','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='clou')
# plt.plot(df.index, df.xs(('vt','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='vt')
# plt.plot(df.index, df.xs(('xsd','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='xsd')
# plt.plot(df.index, df.xs(('soxx','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='soxx')
# plt.plot(df.index, df.xs(('socl','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='socl')
# plt.plot(df.index, df.xs(('ign','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='ign')


plt.plot(df.index, df.xs(('ibuy','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='ibuy')
plt.plot(df.index, df.xs(('ebiz','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='ebiz')
plt.plot(df.index, df.xs(('onln','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='onln')
plt.plot(df.index, df.xs(('socl','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='socl')
plt.plot(df.index, df.xs(('clix','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='clix')
plt.plot(df.index, df.xs(('emqq','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='emqq')
plt.plot(df.index, df.xs(('sgol','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='sgol')
plt.plot(df.index, df.xs(('botz','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='botz')
plt.plot(df.index, df.xs(('clou','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='clou')

plt.legend()
plt.show()