
from repositories.api_mercado_pago import ConfMeLiRepository
import requests

#Mock simples de aprovação de pagamento


class ConfMeLi(ConfMeLiRepository):
    def __init__(self):
        pass

    def gera_qr_code(self, id_pedido: int, valor: float):
        #mock qr code

        #no mercado pago seria utilizado por exemplo
        #string_qr_code = requests.get('https://api.mercadopago.com/instore/orders/qr/seller/collectors/{user_id}/pos/{external_pos_id}/qrs').json()['qr_data']

        string_qr_code = 'string_qr_code'

        return {'qr_code': string_qr_code }
    

    def checa_pagamento(self, id_pedido:int):
        '''checa se um pedido foi pago, versão mock'''

        #via api ficaria na ideia de :

        ## pegando informação de id do pagamento
        #requests.get('https://api.mercadopago.com/v1/payments/search')

        ## filtrando pagamento para obter status
        #result_mercado_pago = requests.get('https://api.mercadopago.com/authorized_payments/{id}').json()['status']


        #mock
        status = True

        return status

