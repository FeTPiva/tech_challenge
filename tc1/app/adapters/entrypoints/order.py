
from app.adapters.entrypoints.model.order_schema import OrderCreation, OrderDetails
from app.adapters.gateway.order import OrderRepository
from app.domain.models.order import Order
from fastapi import APIRouter
from typing import List

router = APIRouter(tags=['Pedido'])


@router.get("/orders", response_model=List[Order])
def read_orders():
    return OrderRepository().get_all_orders()


@router.get("/orders/details", response_model=List[OrderDetails])
def read_orders_details():
    return OrderRepository().get_all_orders_details()


@router.get("/order/{id_pedido}", response_model=Order)
def read_order_by_id(id_pedido:int):
    return OrderRepository().get_order_by_id(id_pedido)


@router.get("/order/details/{id_pedido}", response_model=List[OrderDetails])
def read_order_by_id_details(id_pedido:int):
    return OrderRepository().get_order_by_id_details(id_pedido)


#fake checkout
@router.post("/order/")
def create_order(order: OrderCreation):
    #no mundo real teria que ter validação de pagamento aqui
    return {"id_pedido": OrderRepository().create_order(order)}
