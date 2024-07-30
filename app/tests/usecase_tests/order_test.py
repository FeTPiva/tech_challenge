#import pystest

from usecases.order import OrderUseCase
from entities.models.order import Order
from entities.models.order_itens import OrderItens
from fastapi import HTTPException
from typing import List
import logging


def test_get_all_orders_test():
    result = OrderUseCase().get_all_orders()
    assert type(result) == list

def test_get_order_by_id():
    result = OrderUseCase().get_orders_by_id(1)
    assert type(result) == list

def test_create_order_():
    order = Order(id_pedido=7, ds_status='Frables', id_cliente=2)
    order_item = OrderItens(id_pedido=7, id_produto=2)

    val = OrderUseCase().new_order(order, products=[order_item])

    assert val == 0
   

def test_get_all_orders_sort():
    order = OrderUseCase().get_all_orders_ordered()

    assert type(order) == list   


