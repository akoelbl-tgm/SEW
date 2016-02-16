from unittest import TestCase
from Control import Control
import csv

def csvReader(file_obj, test = False):
        if(test):
            reader = csv.reader(file_obj, delimiter=';')
            for row in reader:
                print(', '.join(row))
        reader = csv.reader(file_obj, delimiter=';')
        return list(reader)

class PythonUnittests(TestCase):

     def test_wrongFileError(self):
        c = Control('asdf.csv')
        self.assertRaises(TypeError, c.read)

     def test_delimiter(self):
        c = Control('testfile.csv')
        c.delimiter = ';'
        self.assertEqual(c.delimiter, ';')

     def test_falseDelimiter(self):
        c = Control('testfile.csv')
        c.delimiter = ' '
        self.assertEqual(c.delimiter, ' ')

     def test_noDelimiter(self):
        c = Control('testfile.csv')
        self.assertIsNone(c.delimiter)

     def test_contentCSV(self):
         with open('testfile2.csv', newline='') as csvFile:
                self.assertEqual(csvReader(csvFile),[['1', '2','3','4']])
