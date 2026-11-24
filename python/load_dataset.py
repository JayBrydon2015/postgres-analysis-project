# -*- coding: utf-8 -*-

"""

Load the dataset into Python with pandas; investigate the columns and their
data types.

"""


import pandas as pd


df = pd.read_csv("datasets/CAS_Data_public.csv")

# Print (# rows, # columns)
print(df.shape)

print()
print()
print()

# Print first few rows
print(df.head())

print()
print()
print()

# Print info, including info about columns and their data types
print(df.info())
