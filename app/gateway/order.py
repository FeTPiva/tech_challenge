from datetime import datetime
from entities.models.order import Order
from external.db_info import ConfDB


class OrderGateway():

    def __init__(self):
        pass

    def get_all_orders(self) -> Order | None:
        return ConfDB().select_all_data('pedido')
    
    def get_orders_by_id(self, id_pedido:int) -> Order | None:
        return ConfDB().select_with_filter(table='pedido', field='id_pedido', value=id_pedido)
    
    def create_order(self, order) -> int:
        return ConfDB().insert_data(table='pedido', data=order)

       
    def update_order(self, pedido) ->  None:        
        return ConfDB().update_data(table='pedido', data=pedido, filter_field='id_pedido', value=pedido['id_pedido'])
    