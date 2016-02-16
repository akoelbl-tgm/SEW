# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CSV_GUI.ui'
#
# Created: Sun Jan 17 20:19:10 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(697, 503)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.delimiterLabel = QtGui.QLabel(self.centralwidget)
        self.delimiterLabel.setGeometry(QtCore.QRect(350, 10, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setWeight(75)
        font.setBold(True)
        self.delimiterLabel.setFont(font)
        self.delimiterLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.delimiterLabel.setObjectName("delimiterLabel")
        self.layoutWidget = QtGui.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 681, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.filenameEingabeTextfeld = QtGui.QLineEdit(self.layoutWidget)
        self.filenameEingabeTextfeld.setObjectName("filenameEingabeTextfeld")
        self.horizontalLayout.addWidget(self.filenameEingabeTextfeld)
        self.oeffneFileButton = QtGui.QPushButton(self.layoutWidget)
        self.oeffneFileButton.setObjectName("oeffneFileButton")
        self.horizontalLayout.addWidget(self.oeffneFileButton)
        self.beendenButton = QtGui.QPushButton(self.layoutWidget)
        self.beendenButton.setObjectName("beendenButton")
        self.horizontalLayout.addWidget(self.beendenButton)
        self.ausgabeText = QtGui.QTextEdit(self.centralwidget)
        self.ausgabeText.setGeometry(QtCore.QRect(10, 80, 681, 411))
        self.ausgabeText.setObjectName("ausgabeText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.beendenButton, QtCore.SIGNAL("clicked()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "File Name (mit Endung .csv) eingeben", None, QtGui.QApplication.UnicodeUTF8))
        self.delimiterLabel.setText(QtGui.QApplication.translate("MainWindow", "Delimiter: -", None, QtGui.QApplication.UnicodeUTF8))
        self.oeffneFileButton.setText(QtGui.QApplication.translate("MainWindow", "Oeffnen", None, QtGui.QApplication.UnicodeUTF8))
        self.beendenButton.setText(QtGui.QApplication.translate("MainWindow", "Beenden", None, QtGui.QApplication.UnicodeUTF8))

