__author__ = 'Alexander Koelbl'
import json

from PySide.QtGui import *
from Jenkins.CSVReader import CSVReader
from MyView import Ui_MainWindow


class Control(QMainWindow):

    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.view = Ui_MainWindow()
        self.view.setupUi(self)
        self.verbindeButtons()

    def verbindeButtons(self):
        self.view.oeffneFileButton.clicked.connect(self.oeffneFile)

    def oeffneFile(self):
        try:
            path = self.view.filenameEingabeTextfeld.text()
            reader = CSVReader(path)
            content = reader.read()
            delimiter = reader.delimiter()
            self.view.delimiterLabel.setText("Delimiter: " + delimiter)
            self.view.ausgabeText.setText(json.dumps(content, indent=4))
        except Exception as e:
            self.view.ausgabeText.setText(e.strerror)
