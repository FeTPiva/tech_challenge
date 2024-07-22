from datetime import datetime
from entities.models.order import Order
from gateway.order import OrderGateway
from gateway.order_itens import OrderItensGateway
from fastapi import HTTPException
from typing import List
from gateway.product import ProductGateway
from entities.models.product import ProductOrder
from datetime import datetime


class OrderUseCase():

    def __init__(self):
        pass

    def get_all_orders(self)  -> Order | None:        
        order_data =  OrderGateway().get_all_orders()

        if order_data:            
            return order_data        
        else:      
            raise HTTPException(status_code=404, detail="Item not found")        
          

    def get_orders_by_id(self, id_pedido: int) -> Order | None:
        order_data =  OrderGateway().get_orders_by_id(id_pedido)
        
        if order_data:            
            return order_data        
        else:      
            raise HTTPException(status_code=404, detail="Item not found")
    
    
    def new_order(self, order: Order , products: List[ProductOrder] ) -> int:
        
        insert_order = order.model_dump()
        #insert_order.pop('id_pedido')
        insert_order['ds_status'] = 'Recebido'
        insert_order['dt_pedido'] = datetime.now()
        insert_order['dt_atualizacao'] = datetime.now()

        order_number =  OrderGateway().create_order(insert_order)
        
        #também é necessário registar os produtos associados ao pedido
        for prod in products:
            order_itens = {'id_pedido': order_number, 'id_produto': prod.id_produto}

            OrderItensGateway().create_order_item(order_itens)

        return order_number       

            
    def update_order_status(self, order: Order) -> Order | None:        

        return OrderGateway().update_order({'ds_status': order.ds_status})

    
    def get_all_orders_ordered(self)  -> Order | None:        
        order_data =  OrderGateway().get_all_orders()

        #ordenando valores
        custom_status_order = {'Recebido': 1, 'Em Preparação': 2, 'Recebido': 3, 'Finalizado': 4}

        sorted_data = sorted(order_data, key=lambda x: (custom_status_order.get(x['ds_status'], float('inf')), x['dt_atualizacao']))

        #filtrando finalizados
        filtered_data = [item for item in sorted_data if item['ds_status'] != 'Finalizado']

        

        if filtered_data:            
            return filtered_data        
        else:      
            raise HTTPException(status_code=404, detail="Item not found")        
          
    

    