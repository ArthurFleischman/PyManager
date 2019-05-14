# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_register.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Register(QMainWindow):
    def __init__(self, mode='r'):
        super().__init__()
        self.mode = mode
        self.setObjectName("MainWindow")
        self.resize(513, 306)
        self.setMinimumSize(QtCore.QSize(513, 306))
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.register_ti1 = QtWidgets.QLineEdit(self.centralwidget)
        self.register_ti1.setText("")
        self.register_ti1.setAlignment(QtCore.Qt.AlignCenter)
        self.register_ti1.setObjectName("register_ti1")
        self.verticalLayout.addWidget(self.register_ti1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.client_de = QtWidgets.QDateEdit(self.centralwidget)
        self.client_de.setObjectName("client_de")
        self.horizontalLayout_2.addWidget(self.client_de)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.register_ti3 = QtWidgets.QLineEdit(self.centralwidget)
        self.register_ti3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.register_ti3.setAlignment(QtCore.Qt.AlignCenter)
        self.register_ti3.setObjectName("register_ti3")
        self.verticalLayout.addWidget(self.register_ti3)
        self.register_ti4 = QtWidgets.QLineEdit(self.centralwidget)
        self.register_ti4.setText("")
        self.register_ti4.setAlignment(QtCore.Qt.AlignCenter)
        self.register_ti4.setObjectName("register_ti4")
        self.verticalLayout.addWidget(self.register_ti4)
        if self.mode != 'e':
            self.register_ti5 = QtWidgets.QLineEdit(self.centralwidget)
            self.register_ti5.setAlignment(QtCore.Qt.AlignCenter)
            self.register_ti5.setObjectName("register_ti5")
            self.verticalLayout.addWidget(self.register_ti5)
            self.register_ti6 = QtWidgets.QLineEdit(self.centralwidget)
            self.register_ti6.setAlignment(QtCore.Qt.AlignCenter)
            self.register_ti6.setObjectName("register_ti6")
            self.verticalLayout.addWidget(self.register_ti6)
        self.register_ti7 = QtWidgets.QLineEdit(self.centralwidget)
        self.register_ti7.setMaximumSize(QtCore.QSize(493, 20))
        self.register_ti7.setAlignment(QtCore.Qt.AlignCenter)
        self.register_ti7.setObjectName("register_ti7")
        self.verticalLayout.addWidget(self.register_ti7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.register_cbox1 = QtWidgets.QComboBox(self.centralwidget)
        self.register_cbox1.setObjectName("register_cbox1")
        self.horizontalLayout.addWidget(self.register_cbox1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.register_btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.register_btn1.setObjectName("register_btn1")
        self.verticalLayout.addWidget(self.register_btn1)
        self.register_btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.register_btn2.setObjectName("register_btn2")
        self.verticalLayout.addWidget(self.register_btn2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Register"))
        self.register_ti1.setPlaceholderText(
            _translate("MainWindow", "Full Name"))
        self.label_2.setText(_translate("MainWindow", "Birthday:"))
        self.register_ti3.setPlaceholderText(_translate("MainWindow", "CPF"))
        self.register_ti4.setPlaceholderText(
            _translate("MainWindow", "Username"))
        if self.mode != 'e':
            self.register_ti5.setPlaceholderText(
                _translate("MainWindow", "Password"))
            self.register_ti6.setPlaceholderText(
                _translate("MainWindow", "Repeat Password"))
        self.register_ti7.setPlaceholderText(
            _translate("MainWindow", "Company"))
        self.label.setText(_translate("MainWindow", "status:"))
        self.register_btn1.setText(_translate("MainWindow", "Register"))
        self.register_btn2.setText(_translate("MainWindow", "Cancel"))
