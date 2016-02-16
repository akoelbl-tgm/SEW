__author__ = 'Alexander Koelbl'
import sys

from PySide.QtGui import *
from Jenkins import Control

if __name__ == "__main__":
    app = QApplication(sys.argv)
    con = Control.Control()
    con.show()
    sys.exit(app.exec_())
