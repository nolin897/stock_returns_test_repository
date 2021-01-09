#Windows command line utility test directory

import pandas as pd
from pandas import read_csv
import csv
import statistics
import numpy as np
from sklearn.linear_model import LinearRegression

print("AAPL Returns")

returns_filepath="AAPL.csv"

returns_df = read_csv(returns_filepath)
print(type(returns_df))
print("Inspect first/last 5 rows:")
print(returns_df.head(5))
print(returns_df.tail(5))

print("--------------------")
print("Counting rows:")
print(len(returns_df))

print("--------------------")
print("Looping through rows:")
for index, row in returns_df.iterrows():
    print(row["Date"])

print("--------------------")
print("Reference a specific row:")
print(returns_df.iloc[0])

#selecting multiple columns yields a dataframe object
print("--------------------")
print("Selecting many columns:")
print(type(returns_df[["Date", "Adj Close"]]))
print(returns_df[["Date", "Adj Close"]])

#selecting one column yields a dataframe object
print("--------------------")
print("Selecting one column:")
print(type(returns_df["Adj Close"]))
print(returns_df["Adj Close"])

print("--------------------")
print("Values:")
print(returns_df["Adj Close"].values)

print("--------------------")
print("Distinct Values:")
print(returns_df["Adj Close"].unique())

print("--------------------")
print("Value Counts:")
print(returns_df["Adj Close"].value_counts())

print("--------------------")
print("Value counts (normalized):")
print(returns_df["Adj Close"].value_counts(normalize=True))

print("--------------------")
print("10-YEAR LOW & 10-YEAR HIGH:")
print("10-year Low", returns_df["Adj Close"].min())
print("10-year High", returns_df["Adj Close"].max())

print("--------------------")
print("CACLULATING RETURNS and Adding them to their CSV files:")

returns_df["AAPL_daily_returns"]=returns_df["Adj Close"].pct_change()

returns_df["AAPL_daily_returns"].to_csv("AAPL.csv", mode='a', header=True)

index_filepath = "VFINX.csv"
index_df = read_csv(index_filepath)
index_df["VFINX_daily_returns"]=index_df["Adj Close"].pct_change()

index_df["VFINX_daily_returns"].to_csv("VFINX.csv", mode='a', header=True)

# print(returns_df["AAPL_daily_returns"].head())
# print(index_df["VFINX_daily_returns"].head())

# print("Geometric MEAN & STANDARD DEVIATION:")
# print("AAPL Returns Geometric Mean:", statistics.geometric_mean(returns_df["AAPL_daily_returns"]))
# print("AAPL Returns Standard Deviation (Volatility):", statistics.stdev(returns_df["AAPL_daily_returns"]))
# print("VFINX Returns Geometric Mean:", statistics.geometric_mean(index_df["VFINX_daily_returns"]))
# print("VFINX Returns Standard Deviation (Volatility):", statistics.stdev(index_df["VFINX_daily_returns"]))

# print("--------------------")
# print("Regression Beta")

# x = np.array(index_df["VFINX_daily_returns"].reshape((-1,1))
# y = np.array(returns_df["AAPL_daily_returns"])

# print(x)
# print(y)

