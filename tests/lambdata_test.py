"""Basic unit tests for lambdata package"""

import unittest
from random import randint

import pandas as pd
from lambdata.helper_functions import LambdataFrame

# URLs for data sources
url1 = "https://raw.githubusercontent.com/cs109/2014_data/master/countries.csv"
url2 = None
url3 = None
url4 = None


class TestLambdataFrameMethods(unittest.TestCase):

    def test_null_count(self):
        df = LambdataFrame(pd.read_csv(url1))
        self.assertEqual(df.null_count(), 0)
        self.assertEqual(LambdataFrame(pd.DataFrame()).null_count(), 0)

    def test_train_test_split(self):
        df = LambdataFrame(pd.read_csv(url1))
        df_train, df_test = df.train_test_split(0.2)
        self.assertEqual(int(0.2*len(df)), len(df_test))
        self.assertEqual(len(df)-int(0.2*len(df)), len(df_train))
        self.assertIsInstance(df_train, LambdataFrame)
        self.assertIsInstance(df_test, LambdataFrame)


if __name__ == '__main__':
    unittest.main()
