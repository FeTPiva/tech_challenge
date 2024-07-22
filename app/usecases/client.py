from datetime import datetime
from entities.models.client import Client
from gateway.client import ClientGateway
from fastapi import HTTPException


class ClientUseCase():

    def __init__(self):
        pass

    def get_all_clients(self)  -> Client | None:        
        client_data =  ClientGateway().get_all_clients()

        if client_data:            
            return client_data        
        else:      
            raise HTTPException(status_code=404, detail="Item not found")
    
    
    def get_client_by_cpf(self, ds_cpf: str) -> Client | None:       
        client_data =  ClientGateway().get_client_by_cpf(ds_cpf=ds_cpf)
        
        if client_data:            
            return client_data
        
        else:      
            raise HTTPException(status_code=404, detail="Item not found")
        
    
    def create_client(self, client: Client) -> None:
        insert_client = client.model_dump()
        insert_client.pop('id_cliente')
        return ClientGateway().create_client(client=insert_client)

    

    