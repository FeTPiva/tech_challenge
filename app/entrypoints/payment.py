from usecases.payment import PaymentUseCase
from entities.models.payment import Payment
from fastapi import APIRouter
from typing import List, Dict
from entities.response_models.payment import CreatePaymentResponse

from fastapi import APIRouter



router = APIRouter(tags=['Pagamento'])


@router.post("/payment/")
def create_payment(pay:Payment) -> CreatePaymentResponse:
    #return {"id_pedido": ProductUseCase().create_product(product)}
    return PaymentUseCase().generate_payment(pay)


@router.get("/payment/")
def get_payment_status(pay_id:int):
    return PaymentUseCase().get_payment_status(pay_id)


@router.put("/payment/webhook/")
def webhook(external_id:int):
    return PaymentUseCase().payment_webhook(external_id=external_id)


