import mysql.connector


class conf_db():
    def __init__(self):
        pass

    def con_mysql(self):
        mydb = mysql.connector.connect(
            host="test",
            user="root",
            password="password",
            database="db"
            )
        
        return mydb
