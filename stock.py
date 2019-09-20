#!/Users/wenhaowu/p3/bin/python
import yfinance as yf
import numpy
import pandas
import pprint
# msft = yf.Ticker("PVTL")

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

# # show financials
# print((msft.financials))

# # show balance sheet
# print(msft.balance_sheet)

# # show cashflow
# print(msft.cashflow)

# # show options expirations
# print(msft.options)

# # get option chain for specific expiration
# opt = msft.option_chain('YYYY-MM-DD')
# # data available via: opt.calls, opt.puts