import yfinance as yf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pprint
import time
import json
import os
import sys
import re

# get the corresponding stocks from local file
with open('list_stock','r') as f:
  stock_list = f.readlines()

# get info of each stock
for each in stock_list:
  one = each.strip()
  # variables setting block
  history_file = "{}_{}.xlsx".format(one,time.strftime("%Y%m%d", time.localtime())) # today's history file
  target_file = "{}/{}".format(one,history_file) # today's history file with relative path
  json_file = "{}_{}.json".format(one,time.strftime("%Y%m%d", time.localtime())) # today's variable file
  target_json = "{}/{}".format(one,json_file) # today's variable file with relative path

  # get stock information block
  if not os.path.exists(one): # check if the corresponding directory exists
    os.mkdir(one) # if there is NO corresponding directory, then create it
  if not os.path.exists(target_json): # check if the variable file exists
    stock = yf.Ticker(one) # call yf API to get the data
    with open(target_json,'w') as f: # create json file
      f.write(str(stock.info)) # save the stock.info as the json file
    df = stock.history(period="max") # get the history behavior of the stock
    df.to_excel(target_file) # save the stock history behavior as Excel file