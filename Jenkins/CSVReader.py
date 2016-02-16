__author__ = 'Alexander Koelbl'
import csv

class CSVReader(object):

    def __init__(self, path):
        self.path = path
        self.dialect = None

    def read(self):
        data = []

        with open(self.path) as csv_file:
            self.dialect = csv.Sniffer().sniff(csv_file.read(1024))
            csv_file.seek(0)
            reader = csv.DictReader(csv_file, dialect=self.dialect)
            for row in reader:
                data.append(row)
        return data

    def delimiter(self):
        return self.dialect.delimiter if self.dialect is not None else None
