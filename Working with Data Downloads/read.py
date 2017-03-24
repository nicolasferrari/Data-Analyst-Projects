# The contents file hold information about the columns of the main file which is CRDC2013_14. This file contain over  columns
import os
print(os.getcwd())
print(os.listdir('data'))
os.listdir('/home/dq/scripts/data')
import pandas as pd
contents = pd.read_csv("data/CRDC2013_14content.csv")
print(contents.head(40))
print(contents.columns)