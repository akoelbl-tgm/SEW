__author__ = 'Alexander Koelbl'
from PySide.QtGui import *
import Control
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    con = Control.Control()
    con.show()
    sys.exit(app.exec_())
