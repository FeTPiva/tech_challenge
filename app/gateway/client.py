from datetime import datetime
from entities.models.client import Client
from external.db_info import ConfDB


class ClientGateway():

    def __init__(self):
        pass


    def get_all_clients(self)  -> Client | None:
        return ConfDB().select_all_data('cliente')  
    
    
    def get_client_by_cpf(self, ds_cpf: int) -> Client | None:       
        return ConfDB().select_one_value(table='cliente', field='ds_cpf',value=ds_cpf)
    
    
    def create_client(self, client: Client) -> None:
        return ConfDB().insert_data(table='cliente', data=client)

    

    