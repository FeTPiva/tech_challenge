
from app.adapters.repositories.client import ClientRepository
from app.domain.models.client import Client
from fastapi import APIRouter

router = APIRouter()



@router.get("/client/{ds_cpf}")
def read_client(ds_cpf: str):
    resp = ClientRepository().get_client_by_cpf(ds_cpf)
    return {"response": resp}

@router.get("/clients")
def read_client():
    resp = ClientRepository().get_all_clients()
    return {"response": resp}

@router.post("/client/")
def create_client(client: Client):
    resp = ClientRepository().create_client(client)
    return {"response": resp}
