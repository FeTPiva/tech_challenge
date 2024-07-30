from datetime import datetime
from entities.models.payment import Payment
from external.db_info import ConfDB
from external.api_mercado_pago import ConfMeLi
from typing import List


class PaymentGateway():

    def __init__(self):
        pass

    def new_payment_db(self, payment_data: Payment) -> None | int:
        return ConfDB().insert_data(table='pagamento', data=payment_data)
    
    
    def new_payment_mp(self, payment_data: Payment) -> int | None:
        external_payment_id = ConfMeLi().create_payment(payment_data)
        return external_payment_id
    
    
    def generate_qr_code(self, external_id:int) -> str:
        return ConfMeLi().generate_qr_code(external_id)
        
    
    def verify_payment_mp(self, external_id: int) -> bool:
        return ConfMeLi().verify_payment_external(external_id)
    
    def verify_payment_db(self, pay_id: int) -> List | None:
        return ConfDB().select_with_filter(table='pagamento', field='id_pagamento', value=pay_id)    

    def update_payment(self, pay: dict, field:str, value:int) -> None:
        return ConfDB().update_data(table='pagamento',data=pay, filter_field=field, value = value)
    
    def get_all_payments(self) -> List:
        a=ConfDB().select_all_data(table='pagamento')
        print(a)
        return a
    
    def get_payment_by_external_id(self, id_pagamento_externo:int) -> List:
        return ConfDB().select_with_filter(table='pagamento', field='id_pagamento_externo', value=id_pagamento_externo)
    
    def get_status_by_order_id(self, id_pedido:int) -> List:
        return ConfDB().select_with_filter(table='pagamento', field='id_pedido', value=id_pedido)

    
    
    