
from usecases.order import OrderUseCase
from entities.models.order import Order
from entities.models.product import ProductOrder
from fastapi import APIRouter
from typing import List, Dict
from entities.response_models.order import *
from fastapi import APIRouter



router = APIRouter(tags=['Pedido'])


@router.get("/orders", response_model=List[Order])
def read_orders():
    return OrderUseCase().get_all_orders()

@router.get("/order/{id_order}", response_model=List[Order])
def read_order(id_order:int):
    return OrderUseCase().get_orders_by_id(id_order)

@router.post("/order/")
def create_order(order: Order, product: List[ProductOrder]):
    return {"id_pedido": OrderUseCase().new_order(order=order, products=product)}


@router.put("/order/status")
def update_order_status(order:Order):
    resp = OrderUseCase().update_order_status(order)
    return {"response": resp}


@router.get("/orders/sorted", response_model=List[Order])
def read_orders():
    return OrderUseCase().get_all_orders_ordered()
