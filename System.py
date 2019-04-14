from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QDateEdit
from PyQt5.QtCore import Qt
import mysql.connector
status = ('adm','employee','client','undefined')

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
        try:
            self.cursor.execute(f'select {x} from {y}')
        except:
            self.mymsg('w', 'ERROR', 'user not found')
        finally:
            val = self.cursor.fetchall()
            return val

    def insert(self, uid, username, password, name, birthday, cpf, status1):
        try:
            self.cursor.execute(f"insert into clients values({uid}, '{username}', '{password}', '{name}', '{birthday}', '{cpf}','{status1}')")
        except:
            self.mymsg.showmsg('w', 'warning', 'wrong values')
        finally:
            self.mymsg.showmsg('m', 'Done!', f'{username} registered')

    def delete(self, tb, uid):
        try:
            self.cursor.execute(f"delete from {tb} where id ='{uid}'")
        except:
            self.mymsg.showmsg('w', 'warning', 'id not found')

        finally:
            self.mymsg.showmsg('m', 'Done!', 'user deleted')

    def update(self, x, y):
        try:
            self.cursor.execute(f"update clients set id = '{x}' where id = '{y}'")
        except:
            self.mymsg.showmsg('w', 'ERROR', 'ERROR')

    def alter(self, x, y):
        try:
            self.cursor.execute(f'alter table {x} {y}')
        except:
            self.mymsg.showmsg('w', 'ERROR', 'ERROR')


class Controller(QtWidgets.QApplication):

    class Msg(QMessageBox):
        def __init__(self):
            pass

        def showmsg(self, type,title, msg):
            if type == 'w':
                self.warning(None, title, msg)
            elif type == 'm':
                self.information(None, title, msg)

    class Login:
        def __init__(self):
            self.win = uic.loadUi('window_login.ui')
            self.win.ti_username.setFocus()
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
            self.luser = mydb.select('username,status', f"clients where username = '{user}' and password = '{passw}' ")
            if not self.luser:
                self.wmessage()
            else:
                self.win.hide()
                self.MenuWindow = Controller.Menu(self.luser[0][0], self.luser[0][1])

        def wmessage(self):
            self.win.lbl.setText("<font color='red'>wrong user or password</font>")

    class Menu:
        def __init__(self, title, status2):
            self.win = uic.loadUi('window_menu.ui')
            self.win.setWindowTitle(f'{title}-{status2}')
            self.win.actionexit.triggered.connect(self.logoff)
            self.win.actionclients.triggered.connect(self.clients)
            self.win.showMaximized()

        def clients(self):
            self.WindowClients = Controller.Clients()

        def logoff(self):
            self.win.close()
            LoginWindow.__init__()

    class Clients:
        def __init__(self):
            self.win = uic.loadUi('window_clients.ui')
            self.refresh()
            self.win.client_btn1.pressed.connect(self.add)
            self.win.client_btn2.pressed.connect(self.remove)
            self.win.client_btn3.pressed.connect(self.close)
            self.cmsg = Controller.Msg()
            self.win.show()

        def add(self):
            self.WindowRegister = Controller.Regsiter()

        def remove(self):
            if self.clients:
                row = self.win.client_lw.currentRow()
                item = (str(self.win.client_lw.item(row).text()))
                uid = mydb.select('id', f"clients where name = '{item}'")
                mydb.delete('clients', f"{uid[0][0]}")
                self.organize()
                self.refresh()
            else:
                self.cmsg.showmsg('w', 'ERROR', 'no clients to delete')
            self.organize()

        def organize(self):
            l1 = mydb.select('id', 'clients')
            x = []
            for w in range(len(l1)):
                x.append(l1[w][0])
            for w in range(len(x)):
                if w + 1 < len(x):
                    while x[w] != (x[w + 1] - 1):
                        x[w + 1] -= 1
                if x[w] != l1[w][0]:
                    mydb.update(f'{x[w]}', f'{l1[w][0]}')

            mydb.alter('clients', f'AUTO_INCREMENT = {x[-1]}')

        def close(self):
            self.win.close()

        def refresh(self):
            self.win.client_lw.clear()
            self.clients = mydb.select('name', "clients where status = 'client' order by name")
            for x in range(len(self.clients)):
                    self.win.client_lw.addItem(self.clients[x][0])


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
            birthday = self.win.client_de.date().toString(Qt.ISODate).split('-')
            birthday = ''.join(birthday)

            cpf = self.win.register_ti3.text()
            username = self.win.register_ti4.text()
            password = self.win.register_ti5.text()
            rpassword = self.win.register_ti6.text()
            status3 = self.win.register_cbox1.currentText()

            qwery = mydb.select('cpf,username', f"clients where cpf = '{cpf}' and username = '{username}' ")

            if not qwery and len(cpf) == 11 and username != '':
                if password == rpassword:
                    mydb.insert('default', username, password, name, birthday, cpf, status3)
                    self.win.close()
                    LoginWindow.MenuWindow.WindowClients.refresh()
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
