#fake external request
from app.domain.ports.external_payment import FakePaymentPort
#from app.domain.ports.
import requests


class FakePaymentRepository(FakePaymentPort):
    def __init__(self) -> None:
        pass

    def get_payment_status(self) -> bool:
        #na vida real faria uma request aqui para pegar o status do pagamento para um pedido especifico de um cliente X
        return True
        
    def get_qrcode(self) -> None:
        #na vida real faria uma request aqui para pegar qr code de um terceiro
        pass

    def fake_checkout(self, id_pedido):
        #assumindo que aqui deve retornar confirmação do pagamento + resumo do pedido
        if self.get_payment_status():        
                      
            pass
        
        pass
