from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Order(BaseModel):
    id_pedido:Optional[int] = Field(10)
    ds_status:str
    dt_pedido:Optional[datetime] = Field(datetime.now())
    id_cliente:Optional[int] = Field(1)
    dt_atualizacao:Optional[datetime] = Field(datetime.now())
