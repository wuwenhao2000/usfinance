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


stock_list = ['qtum','scho','shy','ief','tlt','o','snsr','five','skyy','acwi','vt','xsd','soxx','socl','ign']

# get the stock history from .xlsx file
df_qtum = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='qtum',b=time.strftime("%Y%m%d", time.localtime())))
df_scho = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='scho',b=time.strftime("%Y%m%d", time.localtime())))
df_shy = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='shy',b=time.strftime("%Y%m%d", time.localtime())))
df_ief = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='ief',b=time.strftime("%Y%m%d", time.localtime())))
df_tlt = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='tlt',b=time.strftime("%Y%m%d", time.localtime())))
df_o = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='o',b=time.strftime("%Y%m%d", time.localtime())))
# df_se = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='se',b=time.strftime("%Y%m%d", time.localtime())))
df_snsr = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='snsr',b=time.strftime("%Y%m%d", time.localtime())))
df_five = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='five',b=time.strftime("%Y%m%d", time.localtime())))
df_skyy = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='skyy',b=time.strftime("%Y%m%d", time.localtime())))
df_acwi = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='acwi',b=time.strftime("%Y%m%d", time.localtime())))
df_vt = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='vt',b=time.strftime("%Y%m%d", time.localtime())))
df_xsd = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='xsd',b=time.strftime("%Y%m%d", time.localtime())))
df_soxx = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='soxx',b=time.strftime("%Y%m%d", time.localtime())))
df_socl = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='socl',b=time.strftime("%Y%m%d", time.localtime())))
df_ign = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='ign',b=time.strftime("%Y%m%d", time.localtime())))


# get the beginning time_line  ['qtum','scho','shy','ief','tlt','o','se','snsr','five','skyy','acwi','vt','xsd','soxx','socl','ign']
df_qtum = df_qtum[df_qtum['Date']>=date]
df_scho = df_scho[df_scho['Date']>=date]
df_shy = df_shy[df_shy['Date']>=date]
df_ief = df_ief[df_ief['Date']>=date]
df_tlt = df_tlt[df_tlt['Date']>=date]
df_o = df_o[df_o['Date']>=date]
# df_se = df_se[df_se['Date']>=date]
df_snsr = df_snsr[df_snsr['Date']>=date]
df_five = df_five[df_five['Date']>=date]
df_skyy = df_skyy[df_skyy['Date']>=date]
df_acwi = df_acwi[df_acwi['Date']>=date]
df_vt = df_vt[df_vt['Date']>=date]
df_xsd = df_xsd[df_xsd['Date']>=date]
df_soxx = df_soxx[df_soxx['Date']>=date]
df_socl = df_socl[df_socl['Date']>=date]
df_ign = df_ign[df_ign['Date']>=date]


# set the index of dataframe ['qtum','scho','shy','ief','tlt','o','se','snsr','five','skyy','acwi','vt','xsd','soxx','socl','ign']
df_qtum.set_index('Date',inplace=True)
df_scho.set_index('Date',inplace=True)
df_shy.set_index('Date',inplace=True)
df_ief.set_index('Date',inplace=True)
df_tlt.set_index('Date',inplace=True)
df_o.set_index('Date',inplace=True)

# df_se.set_index('Date',inplace=True)
df_snsr.set_index('Date',inplace=True)
df_five.set_index('Date',inplace=True)
df_skyy.set_index('Date',inplace=True)
df_acwi.set_index('Date',inplace=True)
df_vt.set_index('Date',inplace=True)
df_xsd.set_index('Date',inplace=True)
df_soxx.set_index('Date',inplace=True)
df_socl.set_index('Date',inplace=True)
df_ign.set_index('Date',inplace=True)

# concat multi dataframe into a new one ['qtum','scho','shy','ief','tlt','o','se','snsr','five','skyy','acwi','vt','xsd','soxx','socl','ign']
df = pd.concat([df_qtum,df_scho,df_shy,df_ief,df_tlt,df_o,df_snsr,df_five,df_skyy,df_acwi,df_vt,df_xsd,df_soxx,df_socl,df_ign],axis=1,keys=stock_list)

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




# # ['qtum','scho','shy','ief','tlt','o','se','snsr','five','skyy','acwi','vt','xsd','soxx','socl','ign']
# plt.plot(df.index, df.xs(('qtum','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='qtum')
# plt.plot(df.index, df.xs(('scho','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='scho')
# plt.plot(df.index, df.xs(('shy','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='shy')
# plt.plot(df.index, df.xs(('ief','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='ief')
# plt.plot(df.index, df.xs(('tlt','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='tlt')
# plt.plot(df.index, df.xs(('o','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='o')
# # plt.plot(df.index, df.xs(('se','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='se')
# plt.plot(df.index, df.xs(('snsr','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='snsr')
# plt.plot(df.index, df.xs(('five','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='five')
# plt.plot(df.index, df.xs(('skyy','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='skyy')
# plt.plot(df.index, df.xs(('acwi','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='acwi')
# plt.plot(df.index, df.xs(('vt','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='vt')
# plt.plot(df.index, df.xs(('xsd','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='xsd')
# plt.plot(df.index, df.xs(('soxx','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='soxx')
# plt.plot(df.index, df.xs(('socl','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='socl')
# plt.plot(df.index, df.xs(('ign','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='ign')


plt.plot(df.index, df.xs(('qtum','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='qtum')
plt.plot(df.index, df.xs(('scho','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='scho')
plt.plot(df.index, df.xs(('shy','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='shy')
plt.plot(df.index, df.xs(('ief','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='ief')
plt.plot(df.index, df.xs(('tlt','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='tlt')
plt.plot(df.index, df.xs(('o','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='o')
# plt.plot(df.index, df.xs(('se','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='se')
plt.plot(df.index, df.xs(('snsr','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='snsr')
plt.plot(df.index, df.xs(('five','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='five')
plt.plot(df.index, df.xs(('skyy','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='skyy')
plt.plot(df.index, df.xs(('acwi','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='acwi')
plt.plot(df.index, df.xs(('vt','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='vt')
plt.plot(df.index, df.xs(('xsd','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='xsd')
plt.plot(df.index, df.xs(('soxx','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='soxx')
plt.plot(df.index, df.xs(('socl','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='socl')
plt.plot(df.index, df.xs(('ign','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='ign')

plt.legend()
plt.show()