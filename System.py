from PyQt5.QtWidgets import QApplication, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from window_users import User
from window_login import Login
from window_menu import Menu
from window_register import Register
import datetime as dt
import sys
import Mydb
status = ('adm', 'employee', 'intern', 'undefined')


def write(message=''):
    log = open('log_PyManager.txt', 'a')
    log.write(
        f'{dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")} -> {message}\n')
    print(message)
    log.close()


def read(file=''):
    log = open('log_PyManager.txt', 'r')
    log.read(file)
    log.seek(0)
    log.close()


class Controller(QApplication):

    class Login:
        def __init__(self):
            self.win = Login()
            self.win.btn.clicked.connect(self.match)
            self.checked = False

        def match(self):
            user = self.win.ti_username.text()
            user = user.split("'")
            user = ''.join(user)
            passw = self.win.ti_password.text()
            passw = passw.split("'")
            passw = ''.join(passw)
            self.luser = mydb.select(
                'username,status', f"users where username = '{user}' and password = '{passw}'")
            if not self.luser:
                write(f'"{user}" access denied')
                self.wmessage()
            else:
                if self.win.rbtn.isChecked():
                    self.checked = True
                else:
                    self.checked = False
                self.win.close()
                write(f'"{user}" access allowed')
                self.MenuWindow = Controller.Menu(
                    self.luser[0][0], self.luser[0][1])

        def wmessage(self):
            self.win.lbl.setText(
                "<font color='red'>wrong user or password</font>")

    class Menu:
        def __init__(self, title, statusm):
            self.title = title
            self.win = Menu(statusm)
            # widgets functions
            self.win.actionexit.triggered.connect(self.logoff)
            self.win.actionclients.triggered.connect(self.clients)
            self.win.showMaximized()
            self.win.setWindowTitle(f'{self.title}-{statusm}')

        def clients(self):
            self.WindowUsers = Controller.Users()

        def logoff(self):
            write(f'[{self.title}] log off')
            app.closeAllWindows()
            LoginWindow.win.ti_password.setText('')
            if not LoginWindow.checked:
                LoginWindow.win.ti_username.setText('')
            LoginWindow.win.show()

    class Users:
        def __init__(self):
            self.choice = ''
            self.win = User()
            for x in status:
                if LoginWindow.luser[0][1] == 'employee' and (x == 'adm' or x == 'employee'):
                    continue
                else:
                    self.win.user_cbox.addItem(x)
            self.refresh()
            # widgets functions
            self.win.user_btn1.pressed.connect(self.add)
            self.win.user_btn2.pressed.connect(self.remove)
            self.win.user_btn3.pressed.connect(self.win.close)
            self.win.user_btn4.pressed.connect(self.edit)
            self.choice = self.win.user_cbox.currentTextChanged.connect(
                self.refresh)

        def add(self):
            self.win.close()
            self.WindowRegister = Controller.Register()

        def remove(self):
            if self.users:
                row = self.win.user_lw.currentRow()
                item = (str(self.win.user_lw.item(row).text()))
                item = item.split(' - ')
                uid = mydb.select('id', f"users where username = '{item[0]}'")
                mydb.delete('users', f"{uid[0][0]}")
                write(
                    f'[{LoginWindow.MenuWindow.title}] deleted user "{item[0]}""')
                self.refresh()
            else:
                QMessageBox.warning(None, 'ERROR', 'no clients to delete')

        def edit(self):
            if self.win.user_lw.currentRow() != -1:
                select_username = str((self.win.user_lw.item(
                    self.win.user_lw.currentRow()).text()))
                select_username = select_username.split('-')
                self.data = mydb.select('name, birthday, cpf_cnpj, username, password, status',
                                        f"users where username = '{select_username[0]}'")
                self.win.close()
                self.WindowEdit = Controller.Edit()

        def refresh(self):
            self.win.user_lw.clear()
            self.choice = self.win.user_cbox.currentText()
            self.users = mydb.select(
                'username,name', f"users where status = '{self.choice}' order by name")
            for x in range(len(self.users)):
                self.win.user_lw.addItem(
                    f"{self.users[x][0]} - {self.users[x][1]}")

    class Register:
        def __init__(self):
            self.win = Register()
            for x in status:
                self.win.register_cbox1.addItem(x)
            self.win.register_btn2.pressed.connect(self.close)
            self.win.register_btn1.pressed.connect(self.register)
            self.win.register_btn1.setFocus()

        def register(self):
            name = self.win.register_ti1.text()
            birthday = self.win.client_de.date().toString(Qt.ISODate).split('-')
            birthday = ''.join(birthday)
            cpf_cnpj = self.win.register_ti3.text()
            username = self.win.register_ti4.text()
            password = self.win.register_ti5.text()
            rpassword = self.win.register_ti6.text()
            statusr = self.win.register_cbox1.currentText()

            query = mydb.select(
                'cpf_cnpj,username', f"users where cpf_cnpj = '{cpf_cnpj}' or username = '{username}' ")
            if not query and len(cpf_cnpj) == 11 and username != '' and password == rpassword:
                mydb.insert('users', 'default', username,
                            password, name, birthday, cpf_cnpj, statusr)
                write(
                    f'[{LoginWindow.MenuWindow.title}] registered "{username}" set:\n birthday = {birthday}\n,cpf_cnpj = {cpf_cnpj}\n,password = {password}\n, status = {statusr}\n')
                self.win.close()
                LoginWindow.MenuWindow.WindowUsers.__init__()
            else:
                QMessageBox.warning(None, 'erro', 'erro')

        def close(self):
            self.win.close()
            LoginWindow.MenuWindow.WindowUsers.__init__()

    class Edit:
        def __init__(self):
            self.win = Register()
            self.win.setWindowTitle(
                f'update - {LoginWindow.MenuWindow.WindowUsers.data[0][3]}')
            for x in status:
                self.win.register_cbox1.addItem(x)
            self.win.register_btn2.pressed.connect(self.cancel)
            self.win.register_btn1.pressed.connect(self.update)
            self.win.register_btn1.setFocus()

            self.data = LoginWindow.MenuWindow.WindowUsers.data
            self.win.register_btn1.setText('Save')
            self.win.register_ti1.setText(self.data[0][0])
            self.win.client_de.setDate(self.data[0][1])
            self.win.register_ti3.setText(self.data[0][2])
            self.win.register_ti4.setText(self.data[0][3])
            self.win.register_ti5.setText(self.data[0][4])
            self.win.register_ti4.setReadOnly(True)
            self.win.register_ti6.setText(self.data[0][4])
            self.win.register_cbox1.setCurrentText(self.data[0][5])

        def update(self):
            name = self.win.register_ti1.text()
            birthday = self.win.client_de.date().toString(Qt.ISODate).split('-')
            birthday = ''.join(birthday)
            cpf_cnpj = self.win.register_ti3.text()
            username = self.win.register_ti4.text()
            password = self.win.register_ti5.text()
            rpassword = self.win.register_ti6.text()
            statusr = self.win.register_cbox1.currentText()
            if username == self.data[0][3] and password == rpassword:
                mydb.update(
                    'users', f"name = '{name}',birthday = '{birthday}',cpf_cnpj = '{cpf_cnpj}',password='{password}', status='{statusr}' where username = '{username}'")
                write(
                    f'[{LoginWindow.MenuWindow.title}] edited "{username}" set:\n birthday = {birthday}\n,cpf_cnpj = {cpf_cnpj}\n,password = {password}\n, status = {statusr}\n')
                self.win.close()
                LoginWindow.MenuWindow.WindowUsers.__init__()
            else:
                QMessageBox.warning(None, 'Warning!', 'something is wrong')

        def cancel(self):
            self.win.close()
            LoginWindow.MenuWindow.WindowUsers.__init__()


if __name__ == '__main__':
    app = Controller(sys.argv)
    mydb = Mydb.Mysql('localhost', 'TKfleBR', 'arthuracf')
    write('conection to server succeed')
    mydb.use('register')
    LoginWindow = Controller.Login()
    write('app initialized')
    sys.exit(app.exec_())
