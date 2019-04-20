# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_users.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class User(QMainWindow):
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
        self.user_lw = QtWidgets.QListWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.user_lw.setFont(font)
        self.user_lw.setWhatsThis("")
        self.user_lw.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.user_lw.setInputMethodHints(QtCore.Qt.ImhNone)
        self.user_lw.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.user_lw.setObjectName("user_lw")
        self.verticalLayout_3.addWidget(self.user_lw)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.user_cbox = QtWidgets.QComboBox(self.centralwidget)
        self.user_cbox.setObjectName("user_cbox")
        self.verticalLayout.addWidget(self.user_cbox)
        self.user_btn1 = QtWidgets.QPushButton(self.centralwidget)
        self.user_btn1.setObjectName("user_btn1")
        self.verticalLayout.addWidget(self.user_btn1)
        self.user_btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.user_btn2.setObjectName("user_btn2")
        self.verticalLayout.addWidget(self.user_btn2)
        self.user_btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.user_btn3.setObjectName("user_btn3")
        self.verticalLayout.addWidget(self.user_btn3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Users"))
        self.label.setText(_translate("MainWindow", "Users List"))
        self.user_btn1.setText(_translate("MainWindow", "Add"))
        self.user_btn2.setText(_translate("MainWindow", "Delete"))
        self.user_btn3.setText(_translate("MainWindow", "Close"))

