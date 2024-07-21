from pydantic import BaseModel, Field
from typing import List, Optional


class ReadClientResponse(BaseModel):
    id_cliente: Optional[int] = Field(0)
    ds_nome: Optional[str] = Field('')
    ds_cpf:Optional[str] = Field('')
    ds_email:Optional[str]= Field('')

class CreateClientResponse(BaseModel):
    id_cliente: int
