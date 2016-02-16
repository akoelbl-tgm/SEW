import csv

from CSVReader import CSVReader
from MyView import Ui_MainWindow

class Control():
    def __init__(self):
        self.read = None
        self.delimiter = None

    def fill(self):
        text = ''
        delimiter = ';'

        with open('testfile.csv', newline='') as f:
            reader = csv.reader(f, delimiter=';', quotechar=' ')

            for row in reader:
                text += str(row)+'\n'