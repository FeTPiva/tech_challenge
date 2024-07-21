
import abc
from typing import List, Dict, Any


class ConfMeLiRepository(abc.ABC):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def gera_qr_code(self, id_pedido:int, valor:float) -> Dict:
        pass
    
    @abc.abstractmethod
    def checa_pagamento(self, id_pedido:int) -> bool:
        pass
    