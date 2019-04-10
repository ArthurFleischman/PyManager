from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import mysql.connector
status = ('adm', 'employee', 'client', 'undefined')


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
        self.mymsg = Controller.Msg()

    def use(self, data):
        self.cursor.execute('use '+data)

    def select(self, x, y):
        self.cursor.execute(f'select {x} from {y}')
        val = self.cursor.fetchall()
        return val

    def insert(self, uid, username, password, name, birthday, cpf, status1):
        try:
            self.cursor.execute(f"insert into clients values({uid}, '{username}', '{password}', '{name}', '{birthday}', '{cpf}','{status1}')")
        except:
            self.mymsg.showmsg('w','warning','hi')
        finally:
            self.mymsg.showmsg('m','Done!',f'{username} registered')
            LoginWindow.MenuWindow.WindowRegister.win.close()


class Controller(QtWidgets.QApplication):

    class Msg(QMessageBox):
        def __init__(self):
            pass

        def showmsg(self,type,title,msg):
            if type == 'w':
                self.warning(None, title, msg)
            elif type == 'm':
                self.information(None,title,msg)

    class Login:
        def __init__(self):
            self.win = uic.loadUi('window_login.ui')
            self.win.ti_username.setFocus()
            self.win.show()

            # widgets functions
            self.win.btn.clicked.connect(self.match)

        def match(self):
            user = self.win.ti_username.text()
            passw = self.win.ti_password.text()
            self.luser = mydb.select('username,status', f"clients where username = '{user}' and password = '{passw}' ")
            if not self.luser:
                self.win.lbl.setText('wrong user or password')
            else:
                self.win.close()
                self.MenuWindow = Controller.Menu(self.luser[0][0], self.luser[0][1])

    class Menu:
        def __init__(self, title, status2):
            self.win = uic.loadUi('window_menu.ui')
            self.win.setWindowTitle(f'{title}-{status2}')
            self.win.actionregister.triggered.connect(self.register)
            self.win.actionexit.triggered.connect(self.logoff)
            self.win.show()

        def register(self):
            self.WindowRegister = Controller.Regsiter()

        def logoff(self):
            self.win.close()
            LoginWindow.__init__()

    class Regsiter:
        def __init__(self):
            self.win = uic.loadUi('window_register.ui')
            for x in status:
                self.win.register_cbox1.addItem(x)
            self.win.show()
            self.win.register_btn2.pressed.connect(self.cancel)
            self.win.register_btn1.pressed.connect(self.register)
            self.win.register_btn1.setFocus()
            self.rmsg = Controller.Msg()

        def register(self):
            name = self.win.register_ti1.text()
            birthday = self.win.register_ti2.text()
            cpf = self.win.register_ti3.text()
            username = self.win.register_ti4.text()
            password = self.win.register_ti5.text()
            rpassword = self.win.register_ti6.text()
            status3 = self.win.register_cbox1.currentText()
            qwery = mydb.select('cpf,username', f"clients where cpf = '{cpf}' and username = '{username}' ")

            if not qwery and (len(cpf) == 11 and username != ''):
                if password == rpassword:
                    mydb.insert('default', username, password, name, birthday, cpf, status3)
                else:
                    self.rmsg.showmsg('w','warning','passwords are not alike')
            else:
                self.rmsg.showmsg('w','erro','erro')

        def cancel(self):
            self.win.close()


if __name__ == '__main__':
    mydb = Mysql('localhost', 'TKfleBR', 'arthuracf')
    mydb.use('register')
    app = Controller([])
    LoginWindow = Controller.Login()
    app.exec()
