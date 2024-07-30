from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class Payment(BaseModel):
    id_pagamento:Optional[int] = Field(0)
    val_valor: float
    val_status:int
    id_pagamento_externo:Optional[int] = Field(1)
    id_pedido:int
