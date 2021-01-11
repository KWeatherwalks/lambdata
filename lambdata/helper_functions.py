"""Lambdata - A collection of Data Science helper functions"""

import numpy as np
import pandas as pd

FAVORITE_ANIMALS = ["Cheetah", "Sloth", "Tree Frog", "Zebra"]


def null_count(df):
    """Counts number of null values in a Pandas Dataframe"""
    return df.isnull().sum().sum()
