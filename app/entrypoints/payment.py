from usecases.payment import PaymentUseCase
from entities.models.payment import Payment
from fastapi import APIRouter
from entities.response_models.payment import CreatePaymentResponse
from fastapi import APIRouter


router = APIRouter(tags=['Pagamento'])


@router.get("/payment/")
def get_all_payments():
    return PaymentUseCase().get_all_payments()


@router.get("/payment/{id_pedido}")
def get_payment_status(id_pedido:int):
    return PaymentUseCase().get_payment_status_order(id_pedido)


@router.post("/payment/")
def create_payment(pay:Payment) -> int:
    return PaymentUseCase().generate_payment(pay)


@router.put("/payment/webhook/{external_id}")
def webhook(external_id:int):
    return PaymentUseCase().payment_webhook(external_id=external_id)


