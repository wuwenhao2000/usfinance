#!/Users/wewu/p3/bin/python
import yfinance as yf
import numpy
import pandas 
import pprint
# print (help(yf))
# print (dir(yf))
stock = yf.Ticker("SE")
# pprint.pprint(stock.info)
# print (stock.history(period="max").tail(5))
print (stock.dividends)
# print (help(stock.history))
# for one in (dir(stock)):
#      print (one)
# print (help(stock.dividends))
# print (stock.info)
# for key in dict(stock.info):
#      print("{}, {}".format(key,dict(stock.info)[key]))
#      # print (key),(dict(stock.info)[key])

# get historical market data
# print (stock.history(period="max"))

# # show actions (dividends, splits)
# print (stock.actions)


# # # show dividends
# print (type(stock.dividends))

# # # show splits
# print (type(stock.splits))

# # # show financials
# print (type(stock.financials))

# # # show balance heet
# print (type(stock.balance_sheet))

# # # show cashflow
# print (type(stock.cashflow))

# # show options expirations
# print (stock.options)

# # get option chain for specific expiration
# opt = stock.option_chain('2019-02-02')
# print (opt.calls)
# # data available via: opt.calls, opt.puts