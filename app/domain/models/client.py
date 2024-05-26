from pydantic import BaseModel
from typing import List, Optional


class Client(BaseModel):
    #id_cliente: Optional[int]
    ds_nome: str 
    ds_cpf:str
    ds_email:str