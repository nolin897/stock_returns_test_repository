#Windows command line utility test directory

import pandas as pd
from pandas import read_csv
import csv
import statistics
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)
import math

returns_filepath="AAPL.csv"
index_filepath = "VFINX.csv"

returns_df = pd.read_csv(returns_filepath)
index_df = pd.read_csv(index_filepath)

print(returns_df.head(3))
print("...")
print(returns_df.tail(3))
print(index_df.head(3))
print("...")
print(index_df.tail(3))

print("--------------------")
print("10-YEAR LOW & 10-YEAR HIGH:")
print("AAPL 10-year Low: ", returns_df["Adj Close"].min())
print("AAPL 10-year High: ", returns_df["Adj Close"].max())
print("VFINX 10-year Low: ", index_df["Adj Close"].min())
print("VFINX 10-year High: ", index_df["Adj Close"].max())

print("--------------------")
print("CACLULATING RETURNS...")

returns_df["AAPL_daily_returns"]=returns_df["Adj Close"].pct_change()
index_df["VFINX_daily_returns"]=index_df["Adj Close"].pct_change()

print(returns_df.head(3))
print("...")
print(returns_df.tail(3))
print(index_df.head(3))
print("...")
print(index_df.tail(3))

print("--------------------")
# print("Adding RETURNS to CSV Files...")

# returns_df.to_csv("AAPL.csv", mode='w+', header=True)

# index_df.to_csv("VFINX.csv", mode='w+', header=True)


print("Calculating Cumulative Returns:")

AAPL_cumulative_returns=(returns_df["AAPL_daily_returns"] + 1).cumprod()
VFINX_cumulative_returns=(index_df["VFINX_daily_returns"] + 1).cumprod()

print(AAPL_cumulative_returns.tail())
print(VFINX_cumulative_returns.tail())

#Graphing prices...

# fig, ax=plt.subplots()
# plt.plot(returns_df["Date"], returns_df["Adj Close"])
# plt.xlabel("Date")
# ax.xaxis.set_major_locator(MultipleLocator(500))
# plt.ylabel("Adjusted")
# plt.title("AAPL Price Data")
# plt.show()

# fig, ax=plt.subplots()
# plt.plot(index_df["Date"], index_df["Adj Close"])
# plt.xlabel("Date")
# ax.xaxis.set_major_locator(MultipleLocator(500))
# plt.ylabel("Adjusted")
# plt.title("VFINX Price Data")
# plt.show()

data = [returns_df["Date"], returns_df["Adj Close"], index_df["Adj Close"]]
headers = ["Date", "AAPL Adj Close", "VFINX Adj Close"]
combined_df = pd.concat(data, axis=1, keys=headers)
print(combined_df.tail(5))

# fig, ax=plt.subplots()
# plt.plot(combined_df["Date"], combined_df["AAPL Adj Close"], combined_df["VFINX Adj Close"])
# ax.legend(["AAPL Adj Close", "VFINX Adj Close"])
# plt.xlabel("Date")
# ax.xaxis.set_major_locator(MultipleLocator(500))
# plt.ylabel("Adjusted Close")
# plt.title("AAPL & VFINX Price Data")
# plt.show()

print("--------------------")
print("Regression Beta")
returns_data = [returns_df["Date"], returns_df["AAPL_daily_returns"], index_df["VFINX_daily_returns"]]
returns_headers = ["Date", "AAPL Daily Returns", "VFINX Daily Returns"]
combined_returns_df = pd.concat(returns_data, axis=1, keys=returns_headers).fillna(value=0)

x = combined_returns_df["VFINX Daily Returns"].to_numpy().reshape((-1, 1))
y = combined_returns_df["AAPL Daily Returns"].to_numpy()

model = LinearRegression().fit(x,y)
r_sq = model.score(x, y)
print("Coefficient of determination: ", r_sq)
print("Intercept: ", model.intercept_)
print("Regression beta: ", model.coef_)

print("--------------------")
AAPL_daily_volatility = combined_returns_df["AAPL Daily Returns"].std()
VFINX_daily_volatility = combined_returns_df["VFINX Daily Returns"].std()

print("Daily Volatilities")
print("AAPL Daily Volatility: ", AAPL_daily_volatility)
print("VFINX Daily Volatility: ", VFINX_daily_volatility)

print("Annualized Volatilities")
AAPL_annualized_volatility = AAPL_daily_volatility*math.sqrt(252)
VFINX_annualized_volatility = VFINX_daily_volatility*math.sqrt(252)
print("AAPL Annualized Volatility: ",AAPL_annualized_volatility)
print("VFINX Annualized Volatility: ",VFINX_annualized_volatility) 
