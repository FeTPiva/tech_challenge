#import pystest

from usecases.payment import PaymentUseCase
from entities.models.payment import Payment
from fastapi import HTTPException
from typing import List


def test_generate_pay():
    pay = Payment(ds_status=0, id_pagamento_externo=2, val_valor=123.4)
    result = PaymentUseCase().generate_payment(pay=pay)

    assert result == 4    

def test_pay_status():
    result = PaymentUseCase().get_payment_status_order(1)
    assert type(result) == list


def test_webhook():
    result = PaymentUseCase().payment_webhook(1)
    assert result == None






    
