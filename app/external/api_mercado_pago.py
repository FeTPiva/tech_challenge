
from repositories.api_mercado_pago import ConfMeLiRepository
import requests
import random

#Mock simples de aprovação de pagamento


class ConfMeLi(ConfMeLiRepository):
    def __init__(self):
        pass

    def create_payment(self, payment_data: dict):
        '''mock de criação de order no mercado pago'''

        #cria pagamento no mercado pago
        #body = {} #parse com payment_data
        #external_id = requests.post('https://api.mercadopago.com/v1/payments', body = body).json()['external_id']

        #mock
        external_id = random.randint(1, 100)

        return external_id
    

    def generate_qr_code(self, external_id: int):
        '''mock qr code'''

        #no mercado pago seria utilizado por exemplo
        #string_qr_code = requests.get('https://api.mercadopago.com/instore/orders/qr/seller/collectors/{user_id}/pos/{external_pos_id}/qrs').json()['qr_data']

        string_qr_code = 'string_qr_code'

        return {'qr_code': string_qr_code }
    

    def verify_payment_external(self, external_id:int):
        '''checa se um pedido foi pago, versão mock'''

        #via api ficaria na ideia de :

        ## pegando informação de id do pagamento
        #requests.get('https://api.mercadopago.com/v1/payments/search')

        ## filtrando pagamento para obter status
        #result_mercado_pago = requests.get('https://api.mercadopago.com/authorized_payments/{id}').json()['status']


        #mock
        status = True

        return status

