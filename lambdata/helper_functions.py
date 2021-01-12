"""Lambdata - A collection of Data Science helper functions"""

import numpy as np
import pandas as pd


def null_count(df):
    """Counts number of null values in a Pandas Dataframe"""
    return df.isnull().sum().sum()

def train_test_split(df, frac):
    """Splits Pandas Dataframe into two dataframes"""
    
    df = df.copy()

    # Number of rows to include in test dataframe
    test_size = int(frac*len(df))

    # Set random seed and select random indices
    rng = np.random.RandomState(42)
    rand_rows = rng.choice(list(df.index), size=test_size, replace=False)

    # Split data into training set and testing subsets
    df_test = df.loc[rand_rows]
    df_train = df.drop(labels=rand_rows)

    return df_test, df_train

def randomize(df, seed):
    """Randomizes the order of a Pandas dataframe"""
    return df.sample(len(df), random_state=seed).reset_index(drop=True)

def addy_split(add_series):
    """From a list of addresses, splits each address into city, state, and zip"""
    # TODO - implement
    pass

def abbr_2_st(state_series, abbr_2_st=True):
    # TODO - Implement
    pass

def list_2_series(list_2_series, df):
    # TODO - Implement
    pass

def rm_outlier(df):
    # TODO - Implement
    pass

def split_dates(date_series):

    """Creates month, day and year columns from a dataframe"""
    df = date_series.copy()
    df['month'] = date_series.str.split('/')[0]
    df['day'] = date_series.str.split('/')[1]
    df['year'] = date_series.str.split('/')[2]

    return df
