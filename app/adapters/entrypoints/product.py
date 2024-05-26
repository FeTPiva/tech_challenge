
from app.adapters.repositories.product import ProductRepository
from app.domain.models.product import Product
from fastapi import APIRouter
from typing import List

router = APIRouter(tags=['Produtos'])


@router.get("/products", response_model=List[Product])
def read_products():
    return ProductRepository().get_all_products()


@router.get("/product/{id_categoria}", response_model=List[Product])
def read_product(id_categoria:int):
    return ProductRepository().get_product_by_category(id_categoria)
     

@router.post("/product/")
def create_product(product:Product):
    return {"id_produto": ProductRepository().create_product(product)}


@router.put("/product/")
def update_product(product:Product):
    resp = ProductRepository().update_product(product)
    return {"response": resp}


@router.delete("/product/")
def delete_product(id_produto:int):
    resp = ProductRepository().delete_product(id_produto)
    return {"response": resp}