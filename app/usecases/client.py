from datetime import datetime
from entities.models.client import Client
from gateway.client import ClientGateway
from external.db_info import conf_db
import json



class ClientUseCase():

    def __init__(self):
        pass

    def get_all_clients(self)  -> Client | None:
        return ClientGateway().get_all_clients()  
    
    
    def get_client_by_cpf(self, ds_cpf: str) -> Client | None:       
        return ClientGateway().get_client_by_cpf(ds_cpf=ds_cpf)
    
    def create_client(self, client: Client) -> None:
        insert_client = client.model_dump()
        insert_client.pop('id_cliente')
        return ClientGateway().create_client(client=insert_client)

    

    