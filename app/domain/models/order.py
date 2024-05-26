from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class Order(BaseModel):
    id_pedido:int 
    ds_status:str
    dt_time:datetime
    id_cliente:int

