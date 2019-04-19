# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_clients.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Client(QMainWindow):
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(622, 402)
        self.setMinimumSize(QtCore.QSize(622, 402))
        self.setMaximumSize(QtCore.QSize(622, 402))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.client_lw = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.client_lw.setFont(font)
        self.client_lw.setWhatsThis("")
        self.client_lw.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.client_lw.setInputMethodHints(QtCore.Qt.ImhNone)
        self.client_lw.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.client_lw.setObjectName("client_lw")
        self.verticalLayout_3.addWidget(self.client_lw)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.client_btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.client_btn1.setObjectName("client_btn1")
        self.verticalLayout.addWidget(self.client_btn1)
        self.client_btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.client_btn2.setObjectName("client_btn2")
        self.verticalLayout.addWidget(self.client_btn2)
        self.client_btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.client_btn3.setObjectName("client_btn3")
        self.verticalLayout.addWidget(self.client_btn3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Clients"))
        self.label.setText(_translate("MainWindow", "Client List"))
        self.client_btn1.setText(_translate("MainWindow", "Add"))
        self.client_btn2.setText(_translate("MainWindow", "Delete"))
        self.client_btn3.setText(_translate("MainWindow", "Close"))

