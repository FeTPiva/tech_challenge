
from usecases.client import ClientUseCase
from entities.models.client import Client
from entities.response_models.client import ReadClientResponse, CreateClientResponse
from fastapi import APIRouter
from typing import List

router = APIRouter(tags=['Cliente'])

@router.get("/client/{ds_cpf}", response_model=List[ReadClientResponse])
def read_client(ds_cpf: str):
    return ClientUseCase().get_client_by_cpf(ds_cpf)


@router.get("/clients" , response_model=List[ReadClientResponse])
def read_clients():
    return ClientUseCase().get_all_clients()


@router.post("/client/")
def create_client(client: Client) -> CreateClientResponse:    
    return {"id_cliente": ClientUseCase().create_client(client)}
