from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Order(BaseModel):
    id_pedido:Optional[int] = Field(0)
    ds_status:str
    dt_pedido:Optional[datetime] = Field(datetime.now())
    id_cliente:int
    dt_entrega:Optional[datetime] = Field(datetime.now())

    class Config:
        orm_mode = True
        

class OrderItens(BaseModel):
    id_pedido:int
    id_produto:int

    class Config:
        orm_mode = True