from pydantic import BaseModel, Field
from typing import List, Optional


class ReadClientResponse(BaseModel):
    id_cliente: int 
    ds_nome: str 
    ds_cpf: str
    ds_email:str

class CreateClientResponse(BaseModel):
    id_cliente: int
