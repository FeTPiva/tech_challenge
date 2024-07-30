from datetime import datetime
from entities.models.product import Product
from gateway.product import ProductGateway
from fastapi import HTTPException


class ProductUseCase():

    def __init__(self):
        pass

    def get_all_products(self)  -> Product | None:        
        product_data =  ProductGateway().get_all_products()

        if product_data:            
            return product_data        
        else:      
            raise HTTPException(status_code=404, detail="Item not found")
        
    def get_product_by_category(self, id_categoria: int) -> Product | None:
        product_data =  ProductGateway().get_product_by_category(id_categoria)
        
        if product_data:            
            return product_data
        
        else:      
            raise HTTPException(status_code=404, detail="Item not found")
    

    def get_product_by_id(self, id_produto: int) -> Product | None:
        product_data =  ProductGateway().get_product_by_id(id_produto)
        
        if product_data:            
            return product_data
        
        else:      
            raise HTTPException(status_code=404, detail="Item not found")
    
    
    def create_product(self, produto: Product) -> int:
        insert_product = produto.model_dump()
        insert_product.pop('id_produto')
        return ProductGateway().create_product(insert_product)
    
        
    def update_product(self, produto: Product) -> Product | None:        
        insert_product = produto.model_dump()
        return ProductGateway().update_product(insert_product)

    
    def delete_product(self, id_produto: int) -> None:
        return ProductGateway().delete_product(id_produto)


    

    