from pydantic import BaseModel
from typing import List, Optional

class client(BaseModel):
    id:int
    nome: str 
    cpf:str
    email:str