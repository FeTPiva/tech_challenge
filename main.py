from typing import Union

from fastapi import FastAPI
from app.adapters.repositories.client import ClientRepository
from app.domain.models.client import Client

from app.adapters.repositories.product import ProductRepository
from app.domain.models.product import Product

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/client/{ds_cpf}")
def read_client(ds_cpf: str):
    resp = ClientRepository().get_client_by_cpf(ds_cpf)
    return {"response": resp}

@app.get("/clients")
def read_client():
    resp = ClientRepository().get_all_clients()
    return {"response": resp}

@app.post("/client/")
def create_client(client: Client):
    resp = ClientRepository().create_client(client)
    return {"response": resp}



@app.get("/products")
def read_products():
    resp = ProductRepository().get_all_products()
    return {"response": resp}

@app.get("/product/{id_categoria}")
def read_product(id_categoria:int):
    resp = ProductRepository().get_product_by_category(id_categoria)
    return {"response": resp}

@app.post("/product/")
def create_product(product:Product):
    resp = ProductRepository().create_product(product)
    return {"response": resp}

@app.put("/product/")
def update_product(product:Product):
    resp = ProductRepository().update_product(product)
    return {"response": resp}


@app.delete("/product/")
def delete_product(id_produto:int):
    resp = ProductRepository().delete_product(id_produto)
    return {"response": resp}


