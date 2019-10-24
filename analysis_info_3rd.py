import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pprint
import datetime
import plotly
import cufflinks as cf 
cf.go_offline
from pandas_datareader import data,wb

# set the beginning date of stock dataframe analysis
start = datetime.datetime(2017,1,1)

# set the category of stocks, the items involved here should be in the same field, which will be meaningful
stock_list = ['O','BXP','HCP','VNQ']

# grab the data via data.DataReader with the yahoo as the data source, each stock generates one dataframe
O = data.DataReader('O','yahoo',start)
BXP= data.DataReader('BXP','yahoo',start)
HCP = data.DataReader('HCP','yahoo',start)
VNQ = data.DataReader('VNQ','yahoo',start)

# pd.concat is used to concat dataframes together to generate a new multi_level index dataframe
df = pd.concat([O,BXP,HCP,VNQ],axis=1,keys=stock_list)

# set the column names to multi_level index dataframe
df.columns.names = ['Stock_Name','Stock_INFO']
# print (df.head())

# df.xs is used to grab value with specific column(axis=1) or index(axis=0, default) in multi_level index dataframe
# print (df.xs(key="Close",axis=1,level='Stock_INFO').head()) # get the Close column of all stocks
# print (df.xs(key="O",axis=1,level='Stock_Name').head()) # get the columns of O

# generate a new dataframe named returns
returns = pd.DataFrame()

# get the return of each stock, (Pt - P(t-1))/P(t-1) here the method .pct_change() is used percentage change
for stock in stock_list:
  returns[stock+"_Return"] = df[stock]['Close'].pct_change()
returns = (returns[1:]) # delete the fist row with NaN
# print (returns.max())
# print (returns['O_Return'].idxmin()) # the index of the corresponding value
# print (returns['O_Return'].idxmax()) # the index of the corresponding value
# print (returns.std()) # standard deviation to test the stability, the less the better
# print (returns.loc['2019-01-01':].std())
# sns.distplot(returns.loc['2017-01-01':]['O_Return'],color='green',bins=60)
# sns.distplot(returns.loc['2017-01-01':]['BXP_Return'],color='blue',bins=60)

# df.xs(key="Close",axis=1,level='Stock_INFO').plot(label=stock) # built-in plot
# df.xs(key="Close",axis=1,level='Stock_INFO').iplot() # can not be used 

# print (df.xs(('O','Close'),axis=1,level=('Stock_Name','Stock_INFO'))) # get value from multi_index dataframe

# df.xs(key=('O','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean().plot(label='O avg',color='blue')
# df.xs(key=('O','Close'),axis=1,level=('Stock_Name','Stock_INFO')).plot(label='O Close',color='green')

# generate the sns chart 
# https://seaborn.pydata.org/generated/seaborn.pairplot.html
# sns.pairplot(returns,diag_kind="kde", markers="+")

# plt.plot(df.index, df.xs(('O','Close'),axis=1,level=('Stock_Name','Stock_INFO')).rolling(window=30).mean(),label='O AVG')
# plt.plot(df.index, df.xs(('O','Close'),axis=1,level=('Stock_Name','Stock_INFO')),label='O Close')

sns.heatmap(df.xs(key="Close",axis=1,level='Stock_INFO').corr()) # show the correlationship
# sns.clustermap(df.xs(key="Close",axis=1,level='Stock_INFO').corr(),annot=True)

# heatmap and clustermap must be corr() model
plt.legend()
plt.show()