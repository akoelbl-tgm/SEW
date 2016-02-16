import csv

class Control():
    def __init__(self,filename):
        self.read = None
        self.delimiter = None
        self.csvfile = filename

    def fill(self):
        text = ''
        delimiter = ';'

        with open(self.csvfile, newline='') as f:
            reader = csv.reader(f, delimiter=';', quotechar=' ')
            for row in reader:
                text += str(row)+'\n'