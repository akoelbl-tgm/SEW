__author__ = 'Alexander Koelbl'

from unittest import TestCase
from CSVReader import CSVReader

class PythonUnittests(TestCase):

     def test_reader_none(self):
        reader = CSVReader(None)
        self.assertRaises(TypeError, reader.read)
