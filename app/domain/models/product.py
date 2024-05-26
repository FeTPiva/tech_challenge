
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Product(BaseModel):
    id_produto: Optional[int] = Field(0)
    ds_nome: str
    id_categoria:int    
    val_preco:float
    dt_atualizacao: Optional[datetime] = Field(datetime.now())

