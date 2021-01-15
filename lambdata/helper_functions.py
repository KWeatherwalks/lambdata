"""Lambdata - A collection of Data Science helper functions"""

import numpy as np
import pandas as pd


class LambdataFrame(pd.DataFrame):

    def null_count(self):
        """Counts number of null values in a Dataframe"""
        return self.isnull().sum().sum()

    def train_test_split(self, frac):
        """Splits Pandas Dataframe into two Lambdataframes"""

        # Number of rows to include in test dataframe
        test_size = int(frac*len(self))

        # Set random seed and select random indices
        rng = np.random.RandomState(42)
        rand_rows = rng.choice(list(self.index), size=test_size, replace=False)

        # Split data into training set and testing subsets
        df_test = self.loc[rand_rows]
        df_train = self.drop(labels=rand_rows)

        return df_train, df_test

    def randomize(self, seed):
        """Randomizes the order of a Dataframe"""
        return self.sample(len(self), random_state=seed).reset_index(drop=True)


if __name__ == "__main__":

    def randomize(df, seed):
        """Randomizes the order of a Pandas dataframe"""
        return df.sample(len(df), random_state=seed).reset_index(drop=True)

    def addy_split(add_series):
        """
        From a list of addresses, splits each address into city, state, and zip
        """
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
        # TODO - Implement
        pass
