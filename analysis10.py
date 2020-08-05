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

# important plot lmplot, distplot, pairplot
# https://seaborn.pydata.org/generated/seaborn.lmplot.html
# https://seaborn.pydata.org/generated/seaborn.distplot.html?highlight=sns%20distplot
# https://seaborn.pydata.org/generated/seaborn.pairplot.html?highlight=sns%20pairplot

# import datetime

# beginning date of stock dataframe analysis
date = '2019-01-01'


stock_list = ['vox','socl','ixp']

# get the stock history from .xlsx file
df_vox = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='vox',b=time.strftime("%Y%m%d", time.localtime())))
df_socl = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='socl',b=time.strftime("%Y%m%d", time.localtime())))
df_ixp = pd.read_excel('stock/{a}/{a}_{b}.xlsx'.format(a='ixp',b=time.strftime("%Y%m%d", time.localtime())))

# get the beginning time_line
df_vox = df_vox[df_vox['Date']>=date]
df_socl = df_socl[df_socl['Date']>=date]
df_ixp = df_ixp[df_ixp['Date']>=date]

# set the index of dataframe
df_vox.set_index('Date',inplace=True)
df_socl.set_index('Date',inplace=True)
df_ixp.set_index('Date',inplace=True)

# concat multi dataframe into a new one
df = pd.concat([df_vox,df_socl,df_ixp],axis=1,keys=stock_list)

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







# the historical return
# returns.plot()









# # the density distribution of the Close
# sns.distplot(df.xs(('socl','Close'),axis=1,level=('Stock_Name','Stock_INFO')),color='green',rug=True,bins=220)

# # the density distribution of the return
# sns.distplot(returns['vox_Return'],color='green',rug=True,bins=220) 







# # the grab method of multi index dataframe, and display it with built-in function
# df.xs(('vox','Close'),axis=1,level=('Stock_Name','Stock_INFO')).plot()








# # the relationship of two columns of one dataframe #kind=scatter,hex,reg,kde
# sns.jointplot(x='socl_Return',y='vox_Return',data=returns,kind='reg')

# # show the correlationship of the value of different columns
# sns.pairplot(returns,diag_kind="kde", markers="+")
# sns.pairplot(returns)







# # heatmap and clustermap must be corr() model
# sns.heatmap(df.xs(key="Close",axis=1,level='Stock_INFO').corr())
# sns.clustermap(df.xs(key="Close",axis=1,level='Stock_INFO').corr(),annot=True)






# # window=30 the avg value of the Close 
# # the historical Close price of stocks involved
# df.xs(key="Close",axis=1,level='Stock_INFO').plot() 
# df.xs(key="Close",axis=1,level='Stock_INFO').rolling(window=30).mean().plot() 






# # following is the function to call plt.plot, which is the same as built-in function
# plt.plot(df.index, df.xs(('vox','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='vox AVG')
# plt.plot(df.index, df.xs(('socl','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='socl AVG')
# plt.plot(df.index, df.xs(('ixp','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='ixp AVG')
plt.plot(df.index, df.xs(('vox','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='vox')
plt.plot(df.index, df.xs(('socl','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='socl')
plt.plot(df.index, df.xs(('ixp','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='ixp')



plt.legend()
plt.show()