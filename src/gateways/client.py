
from sqlalchemy.orm import Session

from external.db_conn import conf_db
from entities.schemas.client import Client
from fastapi import Depends

class ClientGateway:
    def __init__(self):
        pass


    def get_all_clients(self):

        return conf_db().select_all_data('cliente')
    

    
    

    

