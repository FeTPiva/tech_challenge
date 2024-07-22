from datetime import datetime
from entities.models.payment import Payment
from gateway.payment import PaymentGateway
from fastapi import HTTPException


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
        status = PaymentGateway().verify_payment_external(external_id)

        if status:
            PaymentGateway().update_payment(pay ={'ds_status':1}, field='id_pagamento_externo', value=external_id)


    def get_payment_status(self, pay_id:int):
        return PaymentGateway().verify_payment_internal(pay_id)


        
