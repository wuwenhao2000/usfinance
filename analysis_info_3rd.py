import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pprint
import datetime
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

# df.xs is used to grab the specific values with column(axis=1) or index(axis=0, default) in multi_level index dataframe
# print (df.xs(key="Close",axis=1,level='Stock_INFO').head())
# print (df.xs(key="O",axis=1,level='Stock_Name').head())

# generate a new dataframe named returns
returns = pd.DataFrame()

# get the return of each stock, (Pt - P(t-1))/P(t-1) here the method .pct_change() is used percentage change
for stock in stock_list:
  returns[stock+"_Return"] = df[stock]['Close'].pct_change()
# print (returns[1:])

# generate the sns chart 
# https://seaborn.pydata.org/generated/seaborn.pairplot.html
sns.pairplot(returns[1:],diag_kind="kde", markers="+")

# plt.plot(returns.index, returns['O_Return'],label='O')
# plt.plot(returns.index, returns['BXP_Return'],label='BXP')
# plt.legend()
plt.show()