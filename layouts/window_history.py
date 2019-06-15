# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_history.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class History(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(758, 473)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 741, 451))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.hverticalleyout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.hverticalleyout.setContentsMargins(0, 0, 0, 0)
        self.hverticalleyout.setObjectName("hverticalleyout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.hlabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.hlabel.setFont(font)
        self.hlabel.setStyleSheet("")
        self.hlabel.setAlignment(QtCore.Qt.AlignCenter)
        self.hlabel.setObjectName("hlabel")
        self.horizontalLayout.addWidget(self.hlabel)
        self.hdataedit = QtWidgets.QDateEdit(self.verticalLayoutWidget)
        self.hdataedit.setObjectName("hdataedit")
        self.horizontalLayout.addWidget(self.hdataedit)
        self.hbtn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hbtn.setObjectName("hbtn")
        self.horizontalLayout.addWidget(self.hbtn)
        self.hbtn1 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.hbtn1.setObjectName("hbtn1")
        self.horizontalLayout.addWidget(self.hbtn1)
        self.hverticalleyout.addLayout(self.horizontalLayout)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(
            self.verticalLayoutWidget)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.hverticalleyout.addWidget(self.plainTextEdit)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "History"))
        self.hlabel.setText(_translate("MainWindow", "Filter"))
        self.hbtn.setText(_translate("MainWindow", "Filter"))
        self.hbtn1.setText(_translate("MainWindow", "No Filter"))
