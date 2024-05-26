
from app.adapters.repositories.client import ClientRepository
from app.domain.models.client import Client
from fastapi import APIRouter
from typing import List

router = APIRouter(tags=['Cliente'])


@router.get("/client/{ds_cpf}",response_model=Client)
def read_client(ds_cpf: str):
    return ClientRepository().get_client_by_cpf(ds_cpf)

@router.get("/clients", response_model=List[Client])
def read_clients():
    return ClientRepository().get_all_clients()

@router.post("/client/")
def create_client(client: Client):
    return {"id_cliente": ClientRepository().create_client(client)}
