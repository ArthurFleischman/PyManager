from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
import sys
import mysql.connector

class Mysql():
    def __init__(self,host,user,passwd):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd
        )
        self.mycursor = self.mydb.cursor()

    def usedatabase(self,db):
        self.mycursor.execute('use '+db)

    def select(self,x,y):
        self.mycursor.execute(f'select {x} from {y}')
        result = self.mycursor.fetchall()
        return result


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        self.title = 'PymManager'
        self.top = 400
        self.left = 400
        self.width = 400
        self.height = 400
        self.icon = "icon path"
        lbl = QLabel('hello world', self)
        lbl.move(0,0)
        self.initwindow()

    def initwindow(self):
        self.setWindowIcon(QtGui.QIcon(self.icon))
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()



if __name__ == '__main__':

    db = Mysql('localhost','user','password')
    db.usedatabase('database')      #use especific database
    val = db.select('*','clients')  #get all data from clients
    print(val)                      #print all data

    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())
