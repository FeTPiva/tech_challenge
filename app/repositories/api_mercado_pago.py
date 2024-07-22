
import abc
from typing import List, Dict, Any


class ConfMeLiRepository(abc.ABC):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def generate_qr_code(self, external_id:int) -> Dict:
        pass
    
    @abc.abstractmethod
    def verify_payment_external(self, external_id:int) -> bool:
        pass

    @abc.abstractmethod
    def create_payment(self, dados_pagamento: dict) ->int:
          pass
    
    
