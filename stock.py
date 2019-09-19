#!/Users/wenhaowu/p3/bin/python
import yfinance as yf
from pprint import pprint
msft = yf.Ticker("PVTL")


# # get stock info
# pprint (msft.info)

# get historical market data
# hist = msft.history(period="max")

pprint (help(msft.history()))

# # show actions (dividends, splits)
# msft.actions

# # show dividends
# msft.dividends

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