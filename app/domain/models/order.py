from pydantic import BaseModel
from typing import List, Optional

class order(BaseModel):
    id:int
    nome:str 
    cpf:str
    email:str
    status:str