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

if __name__ == '__main__':

    db = Mysql('localhost','user','password')
    db.usedatabase('database')      #use especific database
    val = db.select('*','clients')  #get all data from clients or other stuff
    print(val)                      #print all data
