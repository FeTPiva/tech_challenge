
import mysql.connector
import os
from repositories.db_info import ConfDBRepository



class ConfDB(ConfDBRepository):
    def __init__(self):
        pass

    def con_mysql(self):
        mydb = mysql.connector.connect( 
            host="mysql-service",           #localhost
            user="root",
            password="password",
            database="db"
            )
        
        return mydb
    

    def select_all_data(self, table:str):

        connection = self.con_mysql()    
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM {table}")
        myresult = cursor.fetchall()
                   
        
        fields = [field_md[0] for field_md in cursor.description]

        if myresult:            
            return [dict(zip(fields,row)) for row in myresult]
        else:
            return None


    def select_with_filter(self, table:str, field:str, value):
        connection = self.con_mysql()
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM {table} where {field} = '{value}'")

        myresult = cursor.fetchall()

        fields = [field_md[0] for field_md in cursor.description]  

        if myresult:
            
            return [dict(zip(fields,row)) for row in myresult]
        else:
            return None
        
    
    def insert_data(self, table:str, data : dict):
        connection = self.con_mysql()
        
        fields = ','.join(str(d) for d in data.keys())
        values = "'"+"', '".join(str(v) for v in data.values())+"'"

        cursor = connection.cursor()       
        cursor.execute(f"INSERT INTO {table} ( {fields} ) VALUES ({values})")
        connection.commit()

        return cursor.lastrowid
    
    def delete_data(self, table:str, field:str, value):
        connection = self.con_mysql()
        
        cursor = connection.cursor()
        
        cursor.execute(f"delete from {table} where {field} = {value}" )

        connection.commit()

        pass

    def update_data(self, table:str, data:dict, filter_field:str, value):
        connection = self.con_mysql()

        cursor = connection.cursor()

        condition = []
        for key, val in data.items():
            condition.append(f"{key} = '{val}'")

        update_cond = ", ".join(condition)
        
        query = f"update {table} set {update_cond} where {filter_field} = {value}"

        cursor.execute(query)
        connection.commit()
        
        pass

