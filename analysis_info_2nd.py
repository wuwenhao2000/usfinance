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
date = '2018-01-01'

# the list of stocks
stock_list = ['O','BXP','HCP','VNQ']

for one in stock_list:
  # variables setting block
  history_file = "{}_{}.xlsx".format(one,time.strftime("%Y%m%d", time.localtime())) # today's history file
  target_file = "{}/{}".format(one,history_file) # today's history file with relative path
  json_file = "{}_{}.json".format(one,time.strftime("%Y%m%d", time.localtime())) # today's variable file
  target_json = "{}/{}".format(one,json_file) # today's variable file with relative path
  if one=='O':df_O = pd.read_excel(target_file) # get the stock history from .xlsx file
  elif one=='BXP':df_BXP = pd.read_excel(target_file) # get the stock history from .xlsx file
  elif one=='HCP':df_HCP = pd.read_excel(target_file) # get the stock history from .xlsx file
  elif one=='VNQ':df_VNQ = pd.read_excel(target_file) # get the stock history from .xlsx file

df_O = df_O[df_O['Date']>=date]
df_BXP = df_BXP[df_BXP['Date']>=date]
df_HCP = df_HCP[df_HCP['Date']>=date]
df_VNQ = df_VNQ[df_VNQ['Date']>=date]

df_O.set_index('Date',inplace=True)
df_BXP.set_index('Date',inplace=True)
df_HCP.set_index('Date',inplace=True)
df_VNQ.set_index('Date',inplace=True)

df = pd.concat([df_O,df_BXP,df_HCP,df_VNQ],axis=1,keys=stock_list)
print (df.head())
# 'print (df.xs(1,level="Close",axis=1))'
# df.plot.line(x=df.index,y='Close',figsize=(12,3),lw=1)
  # read the local files block
# with open(target_json,'r') as load_f: # get the variable from .json file
#   curr_var = json.loads(json.dumps(eval(load_f.read()))) # transfer the variable from string -> json -> dict

# print (df[df['Date']> '2017-01-01'])
# dfnew = df[['Date','Close']]
# dfold = df[['Date','Close']]
# dfnew['new_time'] = dfnew['Date']-timedelta(days=365)
# dfold['new_time'] = df['Date']
# # print (dfnew)
# # print (dfold)
# df_combine = pd.merge(dfnew,dfold,how='inner',on='new_time').drop(['new_time','Date_y'],axis=1)
# print (df_combine)
# df_combine['eps'] = df_combine['Close_x']-df_combine['Close_y']
# print (df_combine)

# plt.plot(df_combine['Date_x'],df_combine['Close_x'],label='Close',color='purple',lw=2) # set the coordinate
# plt.plot(df_combine['Date_x'],df_combine['eps'],label='esp',color='blue',lw=2) # set the coordinate
# plt.title("Close vs esp") # chart title
# plt.ylabel("parameter") # Y axis label
# plt.xlabel("Time")  # X axis label
# plt.legend()
# plt.show()
# print (df_combine[df_combine['Date_x']=='2018-10-15'])
# # print (df.head(255))

# from_back_to = df[df['Date'].isin(df['Date'].apply(lambda x:x + timedelta(days=365)))]

# print (len(from_back_to.index))
# print (len(df))
# from_back_to.head['esp'] = from_back_to['Close'] - df[df['Date']==(from_back_to['Date'].apply(lambda x:x - timedelta(days=365)))]['Close']
# print (from_back_to.tail())
# print (df.head())
# print (df.tail())


# print (df_1y['Date'].apply(lambda x:x + timedelta(days=-365)))
# df = df.reset_index().drop(['index'],axis=1)
# print (df[df['Date']==(df_1y['Date']+timedelta(days=-365))])

# print (df.apply(df['Date']+timedelta(days=-365)))

# df['eps'] = df['Close'] - df['Close'].apply(df['Date']+timedelta(days=-365))


# sm =  (df[df['Date']=='2011-07-06'])
# print (sm)
# sm  = sm.reset_index(drop=True)
# print (sm)
# df = df.reset_index(drop=True,inplace=True)

# print (df[df['Date']==sm["Date"]])
# df_1y['eps'] = df_1y['Close']-df[df_1y['Date'datetime.now()+ timedelta(days=-365)]]['Close']
# df_1y['PE'] = df_1y['Close']/df_1y['eps']

# df['book'] = curr_var['bookValue'] # get the book value
# df['PB'] = df['Close']/df['book'] # calculate new column "trailingPB = Close/book"
# df['PB%'] = (df['PB'] - df['PB'].min())/(df['PB'].max()-df['PB'].min())*(100) # calculate PB%
# df['Regular%'] = (df['Close'] - df['Close'].min())/(df['Close'].max()-df['Close'].min())*(100) # calculate Regular%
# df['Rollback%'] = (df['Close'].max() - df['Close'])/df['Close'].max()*(100) # calculate Regular%

# if int(curr_var['epsTrailingTwelveMonths'])>0: # when eps is grater than 0
#   df['eps'] = curr_var['epsTrailingTwelveMonths'] # get the eps
#   df['PE'] = df['Close']/df['eps'] # calculate new column "PE = Close/eps"
#   df['PE%'] = (df['PE'] - df['PE'].min())/(df['PE'].max()-df['PE'].min())*(100) # calculate PE%
#   df=df[['Date','Close','PB','PB%','PE','PE%','Rollback%']] # get the result of all history
# else: # when eps is less than 0
#   df=df[['Date','Close','PB','PB%','Rollback%']] # get the result of all history

# # print (df[>time.ctime(curr_var['earningsTimestamp'])][['Date','Close','eps','trailingPE','PE%','Regular%',]]) # get the result from earningsTimestamp
# # print (df[['Date','Close','trailingPB','trailingPE','PE%','PB%','Regular%']]) # get the result of all history
# # print (df[df['Close'] == df['Close'].max()])


# # create the coordinate based on above data
# if sys.argv[2].upper()=='Y': # if Y, then show the picture
#   # x = df['Date'] # set x axis variable
#   # y = df['PB%'] # set y axis variable
#   # plt.title("PB% vs Time") # set picture title
#   plt.xlabel("Time") # set x axis label
#   # plt.ylabel("PB") # set y axis label
#   plt.plot(df['Date'],df['PB%'],label='PB%',color='green',lw=1) # create the coordinate
#   plt.plot(df['Date'],df['Rollback%'],label='Max drawdown',color='purple',lw=1,ls='--')
#   plt.legend()
#   plt.show() # show the coordinate

#   # # fig = plt.figure(num=1, figsize=(15, 8),dpi=80) 
# # fig = plt.figure() 

# # plt.plot(np.arange(0,1,0.1),range(0,10,1))
# # plt.plot(np.arange(0,1,0.1),range(0,20,2))
# # plt.show()

# else: # else, then show the dataframe
#   print (df[df['Date']=='2019-10-08'])
#   # print (df)

# # sns.set_style("whitegrid")  
# # plt.plot(np.arange(10))  
# # plt.show()


# # x = np.linspace(0, 2, 100)

# # plt.plot(x, x, label='linear')
# # plt.plot(x, x**2, label='quadratic')
# # plt.plot(x, x**3, label='cubic')

# # plt.xlabel('x label')
# # plt.ylabel('y label')

# # plt.title("Simple Plot")

# # plt.legend()

# # plt.show()