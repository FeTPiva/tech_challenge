
import mysql.connector
import os


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
    

    def select_all_data(self, table):
        connection = self.con_mysql()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        myresult = cursor.fetchall()
        
        fields = [field_md[0] for field_md in cursor.description]
        return [dict(zip(fields,row)) for row in myresult]


    def select_one_value(self, table, field, value):
        connection = self.con_mysql()
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM {table} where {field} = {value}")

        myresult = cursor.fetchone()

        fields = [field_md[0] for field_md in cursor.description]
        return dict(zip(fields,myresult))
        
    
    def insert_data(self, table:str, data : dict):
        connection = self.con_mysql()

        fields = ','.join(data.keys())
        values = ','.join(str(v) for v in data.values())

        cursor = connection.cursor()

        query = "INSERT INTO %s ( %s ) VALUES (%s)"
        values =  (table, fields, values)
        
        cursor.execute(query, values)
        self.connection.commit()

        return cursor.lastrowid
    
    def delete_data(self, table:str, field, value):
        connection = self.con_mysql()
        
        cursor = connection.cursor()

        cursor.execute(f"delete from {table} where {field} = {value}" )
        self.connection.commit()


        pass

    def update_data(self, table, data, filter_field, value):


        cursor = self.connection.cursor()

        condition = ['dt_atualizacao = CURRENT_TIMESTAMP()']
        for key, val in data.items():
            condition.append(f'{key} = {val}')

        update_cond = ', '.join(condition)

        
        query = """update %s 
        set %s 
        where %s = %s"""
        values = (table, update_cond, filter_field, value)
        cursor.execute(query, values)
        self.connection.commit()
        pass

