from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import Qt
from window_users import User
from window_login import Login
from window_menu import Menu
from window_register import Register
from window_history import History
import datetime as dt
import sys
import Mydb
status = ('adm', 'employee', 'intern', 'undefined')


class Log:
    def __init__(self):
        self.log = open('log_PyManager.txt', 'a+')

    def write(self, message=''):
        self.log.write(
            f'{dt.datetime.now().strftime("[%Y-%m-%d|%H:%M:%S]")}> {message}.\n')

    def reset(self):
        self.log.seek(0)

    def read(self):
        self.text = self.log.read()
        return self.text


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
                mylog.write(f'({user}) access denied')
                self.wmessage()
            else:
                if self.win.rbtn.isChecked():
                    self.checked = True
                else:
                    self.checked = False
                self.win.close()
                mylog.write(f'({user}) access allowed')
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
            self.win.actionhistory.triggered.connect(self.history)
            self.win.showMaximized()
            self.win.setWindowTitle(f'{self.title}-{statusm}')

        def clients(self):
            self.WindowUsers = Controller.Users()

        def logoff(self):
            mylog.write(f'({self.title}) loged off\n')
            app.closeAllWindows()
            LoginWindow.win.ti_password.setText('')
            if not LoginWindow.checked:
                LoginWindow.win.ti_username.setText('')
            LoginWindow.win.show()

        def history(self):
            self.windowhistory = Controller.History()

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
                mylog.write(
                    f'({LoginWindow.MenuWindow.title}) deleted user "{item[0]}""')
                self.refresh()
            else:
                QMessageBox.warning(None, 'ERROR', 'no clients to delete')

        def edit(self):
            if self.win.user_lw.currentRow() != -1:
                select_username = str((self.win.user_lw.item(
                    self.win.user_lw.currentRow()).text()))
                select_username = select_username.split('-')
                self.data = mydb.select('name, birthday, cpf_cnpj, username, status, company',
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
            company = self.win.register_ti7.text()

            query = mydb.select(
                'cpf_cnpj,username', f"users where cpf_cnpj = '{cpf_cnpj}' or username = '{username}' ")
            if not query and len(cpf_cnpj) == 11 and username != '' and password == rpassword:
                mydb.insert('users', 'default', username,
                            password, name, birthday, cpf_cnpj, statusr, company)
                mylog.write(
                    f'({LoginWindow.MenuWindow.title}) registered ({username}) set: birthday = {birthday}, cpf_cnpj = {cpf_cnpj}, password = {password}, status = {statusr}, company = {company}\n')
                self.win.close()
                LoginWindow.MenuWindow.WindowUsers.__init__()
            else:
                QMessageBox.warning(None, 'erro', 'erro')

        def close(self):
            self.win.close()
            LoginWindow.MenuWindow.WindowUsers.__init__()

    class Edit:
        def __init__(self):
            self.win = Register('e')
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
            self.win.register_ti4.setReadOnly(True)
            self.win.register_ti7.setText(self.data[0][5])
            self.win.register_cbox1.setCurrentText(self.data[0][4])

        def update(self):
            name = self.win.register_ti1.text()
            birthday = self.win.client_de.date().toString(Qt.ISODate).split('-')
            birthday = ''.join(birthday)
            cpf_cnpj = self.win.register_ti3.text()
            username = self.win.register_ti4.text()
            statusr = self.win.register_cbox1.currentText()
            company = self.win.register_ti7.text()
            mydb.update(
                'users', f"name = '{name}',birthday = '{birthday}',cpf_cnpj = '{cpf_cnpj}', status='{statusr}', company='{company}' where username = '{username}'")
            mylog.write(
                f'({LoginWindow.MenuWindow.title}) edited ({username}) to: birthday = {birthday}, cpf_cnpj = {cpf_cnpj}, status = {statusr}')
            self.win.close()
            LoginWindow.MenuWindow.WindowUsers.__init__()

        def cancel(self):
            self.win.close()
            LoginWindow.MenuWindow.WindowUsers.__init__()

    class History:
        def __init__(self):
            self.win = History()
            mylog.log.seek(0)
            self.text = mylog.read()
            self.win.plainTextEdit.clear()
            self.win.hdataedit.setDate(dt.date.today())
            self.win.plainTextEdit.insertPlainText(self.text)
            self.win.hbtn.pressed.connect(self.filter)
            self.win.hbtn1.pressed.connect(
                lambda: self.refresh(self.text, 'r'))

        def filter(self):
            date = self.win.hdataedit.date().toString(Qt.ISODate)
            d = []
            end = -1
            init = -1
            get = False
            for x in range(len(self.text)):
                if self.text[x] == '[':
                    init = x
                if self.text[x] == '.':
                    end = x
                    get = True
                if get == True and self.text[init+1:init+11] == date:
                    d.append(self.text[init:end+1])
                    get = False
            self.refresh(d)

        def refresh(self, data=[], mode='n'):
            self.win.plainTextEdit.clear()
            if mode == 'n':
                if data == []:
                    self.win.plainTextEdit.insertPlainText('No Data Available')
                for r in range(len(data)):
                    if data[r] != '':
                        self.win.plainTextEdit.insertPlainText(
                            '{}\n'.format(data[r]))
            elif mode == 'r':
                self.win.plainTextEdit.insertPlainText(self.text)


if __name__ == '__main__':
    mylog = Log()
    app = Controller(sys.argv)
    mydb = Mydb.Mysql('localhost', 'TKfleBR', 'arthuracf')
    mylog.write('conection to server succeed')
    mydb.use('register')
    LoginWindow = Controller.Login()
    mylog.write('app initialized')
    sys.exit(app.exec_())
