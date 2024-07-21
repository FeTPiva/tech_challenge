from datetime import datetime
from entities.models.payment import Payment
from external.db_info import ConfDB
from external.api_mercado_pago import ConfMeLi


class PaymentGateway():

    def __init__(self):
        pass

    def new_payment(self, dados_pagamento: Payment) -> None:
        resp = ConfDB().insert_data(table='pagamento', data=dados_pagamento)
        print(resp)

        qr = ConfMeLi().gera_qr_code()

        return 0
        
    
    def verify_payment(self, id_categoria: int) -> Payment | None:
        return ConfDB().select_with_filter(table='produto', field='id_categoria', value=id_categoria)
    

    def update_payment(self, id_categoria: int) -> Payment | None:
        return ConfDB().select_with_filter(table='produto', field='id_categoria', value=id_categoria)
    
    