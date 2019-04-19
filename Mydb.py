import mysql.connector
from PyQt5.QtWidgets import QMessageBox


# noinspection PyBroadException
class Mysql:
    def __init__(self, host, user, passwd):
        self.mymsg = None
        self.host = host
        self.user = user
        self.passwd = passwd
        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.passwd
            )
        except:
            QMessageBox.warning(None, 'ERROR', 'Unable to connect to server')
        else:
            self.cursor = self.mydb.cursor()

    def use(self, data):
        try:
            self.cursor.execute('use '+data)
        except:
            QMessageBox.warning(None, 'ERROR', 'no table found')

    def select(self, data, table):
        try:
            self.cursor.execute(f'select {data} from {table}')
        except:
            QMessageBox.warning(None, 'ERROR', 'user not found')
        else:
            val = self.cursor.fetchall()
            return val

    def insert(self, table, uid, username, password, name, birthday, cpf, status1):
        try:
            self.cursor.execute(f"insert into {table} values({uid}, '{username}', '{password}', '{name}', '{birthday}', '{cpf}','{status1}')")
        except:
            QMessageBox.warning(None, 'warning', 'wrong values')
        else:
            QMessageBox.information(None, 'Done!', f'{username} registered')

    def delete(self, table, uid):
        try:
            self.cursor.execute(f"delete from {table} where id ='{uid}'")
        except:
            QMessageBox.warning(None, 'ERROR', 'ID not found')

        else:
            QMessageBox.information(None, 'DONE!', 'user deleted')

    def update(self, table, data):
        try:
            self.cursor.execute(f"update {table} set {data}")
        except:
            QMessageBox.warning(None, 'ERROR', 'could not update')

    def alter(self, table, data):
        try:
            self.cursor.execute(f'alter table {table} {data}')
        except:
            QMessageBox.warning(None, 'ERROR', 'could not insert values')
