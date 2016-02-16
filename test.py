__author__ = 'Alexander Koelbl'

from unittest import TestCase
from CSVReader import CSVReader

class PythonUnittests(TestCase):

     def test_reader_none(self):
        reader = CSVReader(None)
        self.assertRaises(TypeError, reader.read)

     def test_reader_number(self):
        reader = CSVReader(123456)
        self.assertRaises(Exception, reader.read)

     def test_reader_invalid_file(self):
         reader = CSVReader("asdf.csv")
         self.assertRaises(FileNotFoundError, reader.read)

     def test_success(self):
         reader = CSVReader("testfile.csv")
         data = reader.read()
         self.assertTrue(len(data) == 3)

     def test_delimiter(self):
         reader = CSVReader("testfile.csv")
         reader.read()
         self.assertEqual(reader.delimiter(), ',')
