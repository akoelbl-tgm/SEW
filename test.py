from unittest import TestCase
from Control import Control

class PythonUnittests(TestCase):

     def test_reader_none(self):
        c = Control()
        self.assertRaises(TypeError, c.read)

     def test_delimiter(self):
        """
        testet ob der richtige delimiter benutzt wird
        """
        c = Control()
        c.delimiter = ';'
        self.assertEqual(c.delimiter, ';')

     def test_non_delimiter(self):
        """
        testet ob ein delimiter vorhanden ist
        """
        c = Control()
        self.assertIsNone(c.delimiter)

     def test_wrong_delimiter(self):
        """
        testet ob ein falscher delimiter verwendet wird
        """
        c = Control()
        c.delimiter = ' '
        self.assertEqual(c.delimiter, ' ')

     def test_wrong_delimiter2(self):
        """
        testet ob ein falscher delimiter verwendet wird
        """
        c = Control()
        c.delimiter = ','
        self.assertEqual(c.delimiter, ',')