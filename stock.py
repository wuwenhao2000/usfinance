<<<<<<< HEAD
<<<<<<< HEAD
#!/Users/wenhaowu/p3/bin/python
=======
#! ~/p3/bin/python
>>>>>>> 4758bc5d3764bb002a5ed4267fab0a33ba373367
import yfinance as yf
from pprint import pprint
msft = yf.Ticker("PVTL")


# # get stock info
# pprint (msft.info)
=======
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
>>>>>>> d4ebe37f19f1679569ce8312c2f49fcf9b8cf40c

# get historical market data
# hist = msft.history(period="max")

pprint (help(msft.history()))

# # show actions (dividends, splits)
# msft.actions

<<<<<<< HEAD
# # show dividends
# msft.dividends
=======

# # # show dividends
# print (type(stock.dividends))
>>>>>>> d4ebe37f19f1679569ce8312c2f49fcf9b8cf40c

# # show splits
# msft.splits

# # show financials
# msft.financials

# # show balance heet
# msft.balance_sheet

# # show cashflow
# msft.cashflow

# # show options expirations
# msft.options

# # get option chain for specific expiration
# opt = msft.option_chain('YYYY-MM-DD')
# # data available via: opt.calls, opt.puts