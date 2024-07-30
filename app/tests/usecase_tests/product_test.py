#import pystest

from usecases.product import ProductUseCase
from entities.models.product import Product
from fastapi import HTTPException
from typing import List
import logging


def test_get_all_products_test():
    result = ProductUseCase().get_all_products()
    assert type(result) == list

def test_get_product_by_category():
    result = ProductUseCase().get_product_by_category(1)
    assert type(result) == list

def test_get_product_by_id():
    result = ProductUseCase().get_product_by_id(2)
    assert type(result) == list

def test_create_product_():
    product = Product(id_categoria=1, ds_descricao='xxxx', ds_nome='abacaxi', val_preco=123.0)
    val = ProductUseCase().create_product(product)

    assert val == 14

def test_update_product():
    product = Product(id_categoria=1, ds_descricao='xxxx', ds_nome='abacaxi', val_preco=123.0)
    val = ProductUseCase().update_product(produto=product)

    assert val == None
   
