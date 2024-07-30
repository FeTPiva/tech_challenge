from external.api_mercado_pago import ConfMeLi
from entities.models.payment import Payment


def test_create_pay():
    pay = Payment(ds_status=0, id_pagamento_externo=2, val_valor=123.4)

    result = ConfMeLi().create_payment(pay.model_dump())

    assert type(result) == int

def test_qr():

    result = ConfMeLi().generate_qr_code(1)

    assert type(result) == dict


def check_pay():
   result =  ConfMeLi().verify_payment_external(1)
   assert result == True