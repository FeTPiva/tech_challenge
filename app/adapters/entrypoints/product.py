
from app.adapters.repositories.product import ProductRepository
from app.domain.models.product import Product
from fastapi import APIRouter

router = APIRouter()


@router.get("/products")
def read_products():
    resp = ProductRepository().get_all_products()
    return {"response": resp}

@router.get("/product/{id_categoria}")
def read_product(id_categoria:int):
    resp = ProductRepository().get_product_by_category(id_categoria)
    return {"response": resp}

@router.post("/product/")
def create_product(product:Product):
    resp = ProductRepository().create_product(product)
    return {"response": resp}

@router.put("/product/")
def update_product(product:Product):
    resp = ProductRepository().update_product(product)
    return {"response": resp}


@router.delete("/product/")
def delete_product(id_produto:int):
    resp = ProductRepository().delete_product(id_produto)
    return {"response": resp}