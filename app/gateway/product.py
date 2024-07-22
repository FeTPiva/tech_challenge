from datetime import datetime
from entities.models.product import Product
from external.db_info import ConfDB


class ProductGateway():

    def __init__(self):
        pass


    def get_all_products(self)  -> Product | None:
        return ConfDB().select_all_data('produto')  
    
    
    def get_product_by_category(self, id_categoria: int) -> Product | None:
        return ConfDB().select_with_filter(table='produto', field='id_categoria', value=id_categoria)
    
    
    def get_product_by_id(self, id_produto: int) -> Product | None:
        return ConfDB().select_with_filter(table='produto', field='id_categoria', value=id_produto)
    
    
    def create_product(self, produto: Product) -> int:
        return ConfDB().insert_data(table='produto', data=produto)
    
        
    def update_product(self, produto: Product) -> Product | None:        
        return ConfDB().update_data(table='produto', data=produto, filter_field='id_produto',value=produto['id_produto'])

    
    def delete_product(self, id_produto: int):
        return ConfDB().delete_data(table='produto', field='id_produto', value=id_produto)


    
    

    