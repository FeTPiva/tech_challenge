
from usecases.product import ProductUseCase
from entities.models.product import Product
from fastapi import APIRouter
from typing import List, Dict
from entities.response_models.product import CreateProductResponse, ReadProductResponse, AlterProductResponse
from fastapi import APIRouter



router = APIRouter(tags=['Produtos'])


@router.get("/products", response_model=List[ReadProductResponse])
def read_products():
    return ProductUseCase().get_all_products()

@router.get("/product/{id_categoria}", response_model=List[ReadProductResponse])
def read_product(id_categoria:int):
    return ProductUseCase().get_product_by_category(id_categoria)


@router.get("/product/{id_produto}", response_model=List[ReadProductResponse])
def read_product(id_produto:int):
    return ProductUseCase().get_product_by_id(id_produto)
     

@router.post("/product/")
def create_product(product:Product) -> CreateProductResponse:
    return {"id_produto": ProductUseCase().create_product(product)}


@router.put("/product/")
def update_product(product:Product) -> AlterProductResponse:
    resp = ProductUseCase().update_product(product)
    return {"response": resp}


@router.delete("/product/")
def delete_product(id_produto:int) -> AlterProductResponse:
    resp = ProductUseCase().delete_product(id_produto)
    return {"response": resp}