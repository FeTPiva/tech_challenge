from datetime import datetime
from entities.models.order_itens import OrderItens
from external.db_info import ConfDB


class OrderItensGateway():

    def __init__(self):
        pass


    def get_all_order_itens(self) -> OrderItens | None:
        return ConfDB().select_all_data('itens_pedido')
    
    def get_orders_by_id_order(self, id_pedido:int) -> OrderItens | None:
        return ConfDB().select_with_filter(table='itens_pedido', field='id_pedido', value=id_pedido)
    
    def create_order_item(self, order_item: OrderItens) -> int:
        return ConfDB().insert_data(table='itens_pedido', data=order_item)
       
    def update_order(self, pedido: OrderItens) -> OrderItens | None:        
        return ConfDB().update_data(table='itens_pedido', data=pedido, filter_field='id_pedido', value=pedido['id_pedido'])
    
