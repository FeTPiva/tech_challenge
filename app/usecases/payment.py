from datetime import datetime
from entities.models.payment import Payment
from gateway.payment import PaymentGateway
from fastapi import HTTPException
from gateway.order import OrderGateway
from entities.models.order import Order
from typing import List


class PaymentUseCase():

    def __init__(self):
        pass

    def generate_payment(self, pay: Payment) -> int:

        insert_pay = pay.model_dump()        

        #cria pagamento externo        
        id_pagamento_externo = PaymentGateway().new_payment_mp(insert_pay)


        #cria pagamento na aplicação (tabela auxiliar)
        insert_pay.pop('id_pagamento')
        insert_pay['id_pagamento_externo'] = id_pagamento_externo

        return PaymentGateway().new_payment_db(insert_pay)
    

    def payment_webhook(self, external_id:int) -> None:
        
        #valida pagamento
        status = PaymentGateway().verify_payment_mp(external_id)

        if status:
            PaymentGateway().update_payment(pay ={'val_status': 1}, field='id_pagamento_externo', value=external_id)

     
        #é necessario atualizar também o status do pedido
        id_pedido = PaymentGateway().get_payment_by_external_id(external_id)[0]['id_pedido']

        order_status = Order(ds_status='Recebido', id_pedido=id_pedido)

        OrderGateway().update_order(pedido=order_status.model_dump())

        pass

    
    def get_payment_status_order(self, order:int) -> List:
        return PaymentGateway().get_status_by_order_id(order)    


    def get_all_payments(self) ->List:
        return PaymentGateway().get_all_payments()
