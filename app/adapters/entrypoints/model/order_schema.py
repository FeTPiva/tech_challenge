from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime
from app.domain.models.order import Order


class OrderCreation(BaseModel):
    id_cliente:int = Field(1)
    list_itens:List[int] = Field([1,2])


class OrderDetails(Order):
    id_produto:int
    ds_nome: str
    val_preco:float
