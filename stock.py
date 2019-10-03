<<<<<<< HEAD
#!/Users/wewu/p3/bin/python
# PE means using all values / earning value
import yfinance as yf
import numpy
import pandas as pd
import pprint
import time
stock = yf.Ticker("PVTL")
# pprint.pprint (stock.info)
# print (stock.info['marketCap'])
# print (stock.info['sharesOutstanding'])
# print (stock.info['regularMarketPrice'])
# print (stock.info['epsTrailingTwelveMonths'])
# print (stock.info['epsForward'])
# print (stock.info['forwardPE'])
# # print (stock.info['trailingPE'])
df = stock.history(period="max")
# print (sample)

# sample.to_excel("SE.xlsx",index=False) # save the df as Excel file without its index written
# sample.to_excel("SE2.xlsx") # save the df as Excel file without its index written

# print (pd.read_excel('SE2.xlsx',sheet_name='Sheet1')) # read the Excel as the pd

# df.to_excel("SE.xlsx",index=False) # save the df as Excel file without its index written

# print (stock.history(period="max").tail(5))
# print (stock.dividends)
# for one in (dir(stock)):
#      print (one)
# print (help(stock.dividends))
# print (stock.info)
# for key in dict(stock.info):
#      print("{}, {}".format(key,dict(stock.info)[key]))
#      # print (key),(dict(stock.info)[key])
=======
#!/Users/wenhaowu/p3/bin/python
import yfinance as yf
import numpy
import pandas
import pprint
# msft = yf.Ticker("PVTL")
>>>>>>> ee9118e5411d3b7be35d23595ab8cd78909a95a3

# get stock info
# pprint (msft.info)

# get historical market data
# stock = msft.history(period="max")
# print (stock)

# stock.to_excel("PVTL-20190920.xlsx",index=True) # save the df as Excel file without its index written

# # show dividends
# print(msft.dividends)

# # show splits
# print(msft.splits)

<<<<<<< HEAD
# # # show financials
# print (stock.financials)

# # # show balance heet
# print (stock.balance_sheet)
=======
# # show financials
# print((msft.financials))

# # show balance sheet
# print(msft.balance_sheet)
>>>>>>> ee9118e5411d3b7be35d23595ab8cd78909a95a3

# # show cashflow
# print(msft.cashflow)

# # show options expirations
# print(msft.options)

# # get option chain for specific expiration
<<<<<<< HEAD
# opt = stock.option_chain('2019-02-02')
# print (opt.calls)
# # data available via: opt.calls, opt.puts

# df =  (pd.read_excel('SE3.xlsx')) # read the Excel as the pd
# df.to_excel("SE3.xlsx") # save the df as Excel file without its index written

# print (df)
# print (df[['Date','Close']])
# df.drop(['Unnamed: 0'],axis=1,inplace=True) # the operation default is temporary, if you want operation permanent, SET inplace=True
# print (df[['Date','Close','trailingPE','Volume']])

# df['Volume%'] = (df['Volume'] - df['Volume'].min())/(df['Volume'].max()-df['Volume'].min())
# df['max'] = df['trailingPE'].max()
# df['min'] = df['trailingPE'].min()
# print (df['trailingPE'].max())
# print (df['trailingPE'].min())
# print (df[['Date','Close','trailingPE','PE%','Regular%']])
# print (df[df['trailingPE'] ==df['trailingPE'].max()])
# print (df[df['trailingPE'] ==df['trailingPE'].min()])
# print (df[df['Date']>'2018-08-21'])[['Date','Close','trailingPE','PE%','Regular%']]

# print (df)
df['trailingPE'] = df['Close']/stock.info['epsTrailingTwelveMonths']
df['PE%'] = (df['trailingPE'] - df['trailingPE'].min())/(df['trailingPE'].max()-df['trailingPE'].min())
df['Regular%'] = (df['Close'] - df['Close'].min())/(df['Close'].max()-df['Close'].min())
print (df[df['Date']>'2018-08-21'][['Date','Close','trailingPE','PE%','Regular%']])

=======
# opt = msft.option_chain('YYYY-MM-DD')
# # data available via: opt.calls, opt.puts
>>>>>>> ee9118e5411d3b7be35d23595ab8cd78909a95a3
