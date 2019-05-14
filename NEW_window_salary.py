# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\daids\OneDrive\Documents\LPAA\widgetSALARY.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.dockWidget = QtWidgets.QDockWidget(self.centralwidget)
        self.dockWidget.setGeometry(QtCore.QRect(100, 30, 621, 461))
        self.dockWidget.setObjectName("dockWidget")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.textBrowser = QtWidgets.QTextBrowser(self.dockWidgetContents)
        self.textBrowser.setGeometry(QtCore.QRect(59, 51, 241, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.dockWidgetContents)
        self.textBrowser_2.setGeometry(QtCore.QRect(59, 101, 241, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.dockWidgetContents)
        self.doubleSpinBox.setGeometry(QtCore.QRect(319, 101, 221, 20))
        self.doubleSpinBox.setMaximum(99999999999.99)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.pushButton = QtWidgets.QPushButton(self.dockWidgetContents)
        self.pushButton.setGeometry(QtCore.QRect(269, 141, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.dockWidgetContents)
        self.lineEdit.setGeometry(QtCore.QRect(320, 60, 221, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.tabWidget = QtWidgets.QTabWidget(self.dockWidgetContents)
        self.tabWidget.setGeometry(QtCore.QRect(10, 200, 611, 237))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.columnView = QtWidgets.QColumnView(self.tab)
        self.columnView.setGeometry(QtCore.QRect(0, 0, 561, 201))
        self.columnView.setObjectName("columnView")
        self.verticalScrollBar_2 = QtWidgets.QScrollBar(self.tab)
        self.verticalScrollBar_2.setGeometry(QtCore.QRect(570, 10, 16, 191))
        self.verticalScrollBar_2.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_2.setObjectName("verticalScrollBar_2")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.columnView_2 = QtWidgets.QColumnView(self.tab_2)
        self.columnView_2.setGeometry(QtCore.QRect(0, 0, 561, 201))
        self.columnView_2.setObjectName("columnView_2")
        self.verticalScrollBar_3 = QtWidgets.QScrollBar(self.tab_2)
        self.verticalScrollBar_3.setGeometry(QtCore.QRect(570, 0, 17, 201))
        self.verticalScrollBar_3.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar_3.setObjectName("verticalScrollBar_3")
        self.tabWidget.addTab(self.tab_2, "")
        self.dockWidget.setWidget(self.dockWidgetContents)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuSal_rio = QtWidgets.QMenu(self.menubar)
        self.menuSal_rio.setObjectName("menuSal_rio")
        MainWindow.setMenuBar(self.menubar)
        self.menubar.addAction(self.menuSal_rio.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">CPF</p></body></html>"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Salário</p></body></html>"))
        self.doubleSpinBox.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.doubleSpinBox.setWhatsThis(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Registrar"))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Salário Bruto"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Salário Líquido"))
        self.menuSal_rio.setTitle(_translate("MainWindow", "Salário"))


