"""A script to test the functions in helper_functions"""

import pandas as pd
import requests

import lambdata.helper_functions as hf

print("Loading DataFrame")
url = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
df = pd.read_csv(url)
print("DataFrame Loaded Successfully")

print('-'*80)

print("Testing function: {}".format(hf.train_test_split))
train, test = hf.train_test_split(df, .80)
print('Training Size:', len(train), "Test Size:", len(test))
print('DataFrame Size:', len(df))

print('-'*80)

print("Testing function: {}".format(hf.randomize))
print(df)
print(hf.randomize(df, 42))

print('-'*80)
print("Creating Date Series ...")
dates = [
    '2000-04-09', '1993-09-07', '2009-10-22', '2000-06-21', '1999-09-03',
    '1998-03-18', '1997-04-12', '2017-09-04', '2015-05-29', '1992-02-11',
    '2002-04-30', '1999-11-09', '1991-12-20', '2007-08-31', '2004-12-21']
date_series = pd.Series(data=dates)
print("... Date Series Created")
print('-'*80)
print("Testing function: {}".format(hf.split_dates))
print(hf.split_dates(date_series))

print('-'*80)
