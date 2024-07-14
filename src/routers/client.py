
from fastapi import APIRouter
from typing import List
from entities.schemas.client import Client
from usecases.client import ClientUseCase

router = APIRouter(tags=['Cliente'])

@router.get("/clients")
def read_clients():
    return {'a' :ClientUseCase().get_all_clients()}

