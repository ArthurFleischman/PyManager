# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow


class Menu(QMainWindow):

    def __init__(self, cstatus):
        super().__init__()
        self.cstatus = cstatus
        self.setObjectName("MainWindow")
        self.resize(739, 457)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 739, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        self.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.actionsalary = QtWidgets.QAction(self)
        self.actionsalary.setObjectName("actionsalary")
        self.actionhistory = QtWidgets.QAction(self)
        self.actionhistory.setObjectName("actionhistory")
        self.actionclients = QtWidgets.QAction(self)
        self.actionclients.setObjectName("actionclients")
        self.actionexit = QtWidgets.QAction(self)
        self.actionexit.setObjectName("actionexit")
        self.actionprofile = QtWidgets.QAction(self)
        self.actionprofile.setObjectName("actionprofile")

        # actions
        self.menuMenu.addAction(self.actionprofile)
        if self.cstatus == 'adm' or self.cstatus == 'employee':
            self.menuMenu.addAction(self.actionhistory)
            self.menuMenu.addAction(self.actionclients)
            if self.cstatus == 'adm':
                self.menuMenu.addAction(self.actionsalary)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionexit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
        self.show()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        if self.cstatus == 'adm' or self.cstatus == 'employee':
            self.actionsalary.setText(_translate("MainWindow", "Salary"))
            self.actionhistory.setText(_translate("MainWindow", "History"))
            self.actionclients.setText(_translate("MainWindow", "Users"))
        self.actionexit.setText(_translate("MainWindow", "Logoff"))
        self.actionprofile.setText(_translate("MainWindow", "Profile"))
