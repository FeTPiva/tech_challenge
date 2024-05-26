from datetime import datetime


from app.domain.models.client import Client
from app.domain.ports.client import ClientPort
from app.configs.db_info import conf_db
import json


class ClientRepository(ClientPort):

    def __init__(self):
        self.connection = conf_db().con_mysql()


    def get_all_clients(self)  -> Client | None:
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM cliente")
        myresult = cursor.fetchall()
        
        fields = [field_md[0] for field_md in cursor.description]
        result = [dict(zip(fields,row)) for row in myresult]

        if result:
            return result
        return None   
    
    
    def get_client_by_cpf(self, ds_cpf: int) -> Client | None:       
       
        cursor = self.connection.cursor()

        cursor.execute(f"SELECT * FROM cliente where ds_cpf = {ds_cpf}")

        myresult = cursor.fetchone()

        fields = [field_md[0] for field_md in cursor.description]
        result = dict(zip(fields,myresult))

        if result:
            return result
        return None
    
    def create_client(self, client: Client) -> None:
        ds_nome = client.ds_nome
        ds_cpf = client.ds_cpf
        ds_email = client.ds_email

        cursor = self.connection.cursor()

        query = "INSERT INTO cliente ( ds_cpf, ds_nome, ds_email ) VALUES (%s, %s, %s)"
        values =  (ds_cpf, ds_nome, ds_email)
        
        cursor.execute(query, values)
        self.connection.commit()

        return cursor.lastrowid

    

    