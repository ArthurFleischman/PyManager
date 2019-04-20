# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window_menu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

class Menu(QMainWindow):
    def setupUi(self,cstatus):
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
        self.actionStock = QtWidgets.QAction(self)
        self.actionStock.setObjectName("actionStock")
        self.actionhistory = QtWidgets.QAction(self)
        self.actionhistory.setObjectName("actionhistory")
        self.actionclients = QtWidgets.QAction(self)
        self.actionclients.setObjectName("actionclients")
        self.actionexit = QtWidgets.QAction(self)
        self.actionexit.setObjectName("actionexit")
        self.actionbuy = QtWidgets.QAction(self)
        self.actionbuy.setObjectName("actionbuy")
        self.actionprofile = QtWidgets.QAction(self)
        self.actionprofile.setObjectName("actionprofile")
        #actions
        self.menuMenu.addAction(self.actionprofile)
        if self.cstatus == 'adm' or self.cstatus == 'employee':
            self.menuMenu.addAction(self.actionStock)
            self.menuMenu.addAction(self.actionhistory)
            self.menuMenu.addAction(self.actionclients)
        self.menuMenu.addAction(self.actionbuy)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.actionexit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuMenu.setTitle(_translate("MainWindow", "Menu"))
        if self.cstatus == 'adm' or self.cstatus == 'employee':
            self.actionStock.setText(_translate("MainWindow", "Stock"))
            self.actionhistory.setText(_translate("MainWindow", "History"))
            self.actionclients.setText(_translate("MainWindow", "Users"))
        self.actionexit.setText(_translate("MainWindow", "Logoff"))
        self.actionbuy.setText(_translate("MainWindow", "Shop"))
        self.actionprofile.setText(_translate("MainWindow", "Profile"))

