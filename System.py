from PyQt5 import QtWidgets, uic
import mysql.connector


class Mysql:
    def __init__(self, host, user, passwd):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.mydb = mysql.connector.connect(
            host=self.host,
            user=self.user,
            passwd=self.passwd
        )
        self.cursor = self.mydb.cursor()

    def use(self, data):
        self.cursor.execute('use '+data)

    def select(self, x, y):
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
        user = self.window.ti_username.text()
        passw = self.window.ti_password.text()
        luser = mydb.select('username,status', f"clients where username = '{user}' and password = '{passw}' ")
        if not luser:
            self.window.lbl.setText('wrong user or password')
        else:
            self.window.lbl.setText(f'welcome {luser[0][0]}')


if __name__ == '__main__':
    mydb = Mysql('localhost', 'TKfleBR', 'arthuracf')
    mydb.use('register')
    app = QtWidgets.QApplication([])
    win = Login()
    app.exec()
