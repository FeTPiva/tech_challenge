#import pystest

from usecases.client import ClientUseCase
from entities.models.client import Client
from fastapi import HTTPException
from typing import List


def test_get_all_clients_test():
    result = ClientUseCase().get_all_clients()
    assert type(result) == list

def test_get_client_by_cpf():
    result = ClientUseCase().get_client_by_cpf('007.029.330-90')
    assert type(result) == list

def test_create_client_():
    cliente = Client(ds_nome='nome',ds_cpf='007.029.330-90', ds_email='email@')

    assert ClientUseCase().create_client(cliente) == 3



    
