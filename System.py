from PyQt5 import QtWidgets,uic
import mysql.connector
'''
app = QtWidgets.QApplication([])
dlg = uic.loadUi('window.ui')
dlg.ti_username.setFocus()
dlg.show()
app.exec()'''

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
        self.cursor = self.mydb.cursor()

    def use(self,data):
        self.cursor.execute('use '+data)

    def select(self,x,y):
        self.cursor.execute(f'select {x} from {y}')
        val = self.cursor.fetchall()
        return val


class Login:
    def __init__(self):
        self.window = uic.loadUi('window.ui')
        self.window.ti_username.setFocus()
        self.window.show()

        # widgets functions
        self.window.btn.clicked.connect(self.match)

    def match(self):
        luser = mydb.select('username,password,adm','clients')
        user = self.window.ti_username.text()
        passw = self.window.ti_username.text()

        for x in range(len(luser)):
            if user == luser[x][0] and passw == luser[x][1]:
                self.window.lbl.setText('welcome '+luser[x][1])
                break
            elif x == len(luser)-1:
                self.window.lbl.setText('wrong user or password')

#future menu window
class Menu():
    def __init__(self):
        self.window = uic.loadUi('')


if __name__ == '__main__':
    mydb = Mysql('localhost','TKfleBR','arthuracf')
    mydb.use('register')
    app = QtWidgets.QApplication([])
    win = Login()
    app.exec()

