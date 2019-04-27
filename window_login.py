# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_login.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName("MainWindow")
        self.resize(198, 150)
        self.setMinimumSize(QtCore.QSize(198, 150))
        self.setMaximumSize(QtCore.QSize(198, 150))
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.setAutoFillBackground(False)
        self.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.ti_username = QtWidgets.QLineEdit(self.centralwidget)
        self.ti_username.setFrame(False)
        self.ti_username.setObjectName("ti_username")
        self.verticalLayout.addWidget(self.ti_username)
        self.ti_password = QtWidgets.QLineEdit(self.centralwidget)
        self.ti_password.setFrame(False)
        self.ti_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ti_password.setObjectName("ti_password")
        self.verticalLayout.addWidget(self.ti_password)
        self.lbl = QtWidgets.QLabel(self.centralwidget)
        self.lbl.setMinimumSize(QtCore.QSize(133, 26))
        self.lbl.setMaximumSize(QtCore.QSize(133, 26))
        self.lbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lbl.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout.addWidget(self.lbl)
        self.rbtn = QtWidgets.QRadioButton(self.centralwidget)
        self.rbtn.setObjectName("rbtn")
        self.verticalLayout.addWidget(self.rbtn)
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setAutoDefault(True)
        self.btn.setDefault(False)
        self.btn.setFlat(False)
        self.btn.setObjectName("btn")
        self.verticalLayout.addWidget(self.btn)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Login"))
        self.ti_username.setPlaceholderText(_translate("MainWindow", "Username"))
        self.ti_password.setPlaceholderText(_translate("MainWindow", "Password"))
        self.lbl.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.rbtn.setText(_translate("MainWindow", "Remember me"))
        self.btn.setText(_translate("MainWindow", "Login"))

