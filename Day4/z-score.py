#!/usr/bin/python

# Importing pandas library
import pandas as pd

# Getting the file from the user
file = input("Enter your csv file name:\n")

# Reading the file from the user and saving it as data frame in 'df'
df = pd.read_csv(file)

# Getiing the list of columns form the data frame
cols = list(df.columns)

# Removing the serial number from the list of columns to calculate z-score
cols.remove('S.No')

# Looping through every column
for col in cols:

# Creating new column with the original name of the column and "_zscore"
    col_zscore = col + '_zscore'

# For the new column created apply the z-score calculation formula for every cell in that column
    df[col_zscore] = (df[col] - df[col].mean())/df[col].std(ddof=0)

# Print the new data frame
print(df)