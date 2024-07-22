
from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime

class OrderItens(BaseModel):
    id_pedido:int
    id_produto:int
