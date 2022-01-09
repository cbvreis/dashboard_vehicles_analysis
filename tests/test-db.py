from unittest import TestCase
import pandas as pd
from database import Database

data_base = Database()
data_base.connect()


class TestDatabase(TestCase):
    def test_database(self):
        self.assertFalse(data_base.is_connected())


class TestData(TestCase):
    def test_read_pandas(self):
        self.assertIsInstance(data_base.read_pandas(), pd.DataFrame)

    def test_read_pandas_consumo(self):
        self.assertIsInstance(data_base.read_pandas_consumo(), pd.DataFrame)
