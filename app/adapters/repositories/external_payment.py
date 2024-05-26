#fake external request
from app.domain.ports.external_payment import FakePaymentPort
import requests


class FakePaymentRepository(FakePaymentPort):
    def __init__(self) -> None:
        pass

    def get_payment_status() -> bool:
        #na vida real faria uma request aqui para pegar o status do pagamento
        return True
        
    def get_qrcode() -> None:
        pass
    


    