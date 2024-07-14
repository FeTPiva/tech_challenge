from pydantic import BaseModel, Field
from typing import List, Optional


class Client(BaseModel):
    id_cliente: Optional[int] = Field(1)
    ds_nome: str 
    ds_cpf:str
    ds_email:str

    class Config:
        orm_mode = True