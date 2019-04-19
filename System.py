from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from window_clients import Client
from window_login import Login
from window_menu import Menu
from window_register import Register
import sys
import Mydb
status = ('adm', 'employee', 'client', 'undefined')


class Controller(QApplication):
    class Login:
        def __init__(self):
            self.win = Login()
            self.win.setupUi()
            self.win.show()
            # widgets functions
            self.win.btn.clicked.connect(self.match)

        def match(self):
            user = self.win.ti_username.text()
            user = user.split("'")
            user = ''.join(user)
            passw = self.win.ti_password.text()
            passw = passw.split("'")
            passw = ''.join(passw)
            self.luser = mydb.select('username,status', f"users where username = '{user}' and password = '{passw}' ")
            if not self.luser:
                self.wmessage()
            else:
                self.win.hide()
                self.MenuWindow = Controller.Menu(self.luser[0][0], self.luser[0][1])

        def wmessage(self):
            self.win.lbl.setText("<font color='red'>wrong user or password</font>")

    class Menu:
        def __init__(self, title, statusm):
            self.win = Menu()
            self.win.setupUi(statusm)
            self.win.setupUi(statusm)
            self.win.show()
            # widgets functions
            self.win.actionexit.triggered.connect(self.logoff)
            self.win.actionclients.triggered.connect(self.clients)
            self.win.showMaximized()
            self.win.setWindowTitle(f'{title}-{statusm}')
            self.luser = ''

        def clients(self):
            self.WindowClients = Controller.Clients()

        def logoff(self):
            self.win.close()
            LoginWindow.__init__()

    class Clients:
        def __init__(self):
            self.win = Client()
            self.win.setupUi()
            self.win.show()
            self.refresh()
            # widgets functions
            self.win.client_btn1.pressed.connect(self.add)
            self.win.client_btn2.pressed.connect(self.remove)
            self.win.client_btn3.pressed.connect(self.close)

        def add(self):
            self.WindowRegister = Controller.Register()

        def remove(self):
            if self.clients:
                row = self.win.client_lw.currentRow()
                item = (str(self.win.client_lw.item(row).text()))
                uid = mydb.select('id', f"users where name = '{item}'")
                mydb.delete('users', f"{uid[0][0]}")
                self.refresh()
            else:
                QMessageBox.warning(None, 'ERROR', 'no clients to delete')

        def close(self):
            self.win.close()

        def refresh(self):
            self.win.client_lw.clear()
            self.clients = mydb.select('name', "users where status = 'client' order by name")
            for x in range(len(self.clients)):
                    self.win.client_lw.addItem(self.clients[x][0])

    class Register:
        def __init__(self):
            self.win = Register()
            self.win.setupUi()
            self.win.show()
            for x in status:
                self.win.register_cbox1.addItem(x)
            self.win.register_btn2.pressed.connect(self.cancel)
            self.win.register_btn1.pressed.connect(self.register)
            self.win.register_btn1.setFocus()

        def register(self):
            name = self.win.register_ti1.text()
            birthday = self.win.client_de.date().toString(Qt.ISODate).split('-')
            birthday = ''.join(birthday)
            cpf = self.win.register_ti3.text()
            username = self.win.register_ti4.text()
            password = self.win.register_ti5.text()
            rpassword = self.win.register_ti6.text()
            statusr = self.win.register_cbox1.currentText()

            query = mydb.select('cpf,username', f"users where cpf = '{cpf}' or username = '{username}' ")
            if not query and len(cpf) == 11 and username != '' and password == rpassword:
                mydb.insert('users','default', username, password, name, birthday, cpf, statusr)
                self.win.close()
                LoginWindow.MenuWindow.WindowClients.refresh()
            else:
                QMessageBox.warning(None,'erro','erro')

        def cancel(self):
            self.win.close()


if __name__ == '__main__':
    app = Controller(sys.argv)
    mydb = Mydb.Mysql('localhost', 'TKfleBR', 'arthuracf')
    mydb.use('register')
    LoginWindow = Controller.Login()
    sys.exit(app.exec_())
