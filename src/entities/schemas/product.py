
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Product(BaseModel):
    
    id_produto: Optional[int] = Field(1)
    ds_nome: str
    id_categoria:int = Field(1)
    val_preco:float = Field(10.0)
    #dt_atualizacao: Optional[datetime] = Field(datetime.now())
    
    
    class Config:
        orm_mode = True
