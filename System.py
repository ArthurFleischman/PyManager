from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'PymManager'
        self.top = 400
        self.left = 400
        self.width = 400
        self.height = 400
        self.icon = "icon path"
        self.initwindow()

    def initwindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())