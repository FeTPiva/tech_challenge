
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class ReadProductResponse(BaseModel):
    id_produto: int
    ds_nome: str
    id_categoria:int 
    val_preco:float 
    ds_descricao:str
    

class CreateProductResponse(BaseModel):
    id_produto: int


class AlterProductResponse(BaseModel):
    response: Optional[str] = 'null'
