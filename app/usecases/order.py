from datetime import datetime
from entities.models.order import Order
from gateway.order import OrderGateway
from gateway.order_itens import OrderItensGateway
from fastapi import HTTPException
from typing import List
from gateway.product import ProductGateway
from entities.models.product import ProductOrder
from datetime import datetime
from .payment import PaymentUseCase
from .product import ProductUseCase
from entities.models.payment import Payment


class OrderUseCase():

    def __init__(self):
        pass

    def get_all_orders(self)  -> List | None:        
        order_data =  OrderGateway().get_all_orders()

        if order_data:            
            return order_data        
        else:      
            raise HTTPException(status_code=404, detail="Item not found")        
          

    def get_orders_by_id(self, id_pedido: int) -> List | None:
        order_data =  OrderGateway().get_orders_by_id(id_pedido)
        
        if order_data:            
            return order_data        
        else:      
            raise HTTPException(status_code=404, detail="Item not found")
    
    
    def new_order(self, order: Order , products: List[ProductOrder] ) -> int:
        
        insert_order = order.model_dump()
        insert_order.pop('id_pedido')
        insert_order['ds_status'] = 'Aguardando Pagamento'
        insert_order['dt_pedido'] = datetime.now()
        insert_order['dt_atualizacao'] = datetime.now()

        order_number =  OrderGateway().create_order(insert_order)
        
        #também é necessário registar os produtos associados ao pedido e valor total da compra
        total_value = 0
        for prod in products:
            order_itens = {'id_pedido': order_number, 'id_produto': prod.id_produto}

            total_value += ProductUseCase().get_product_by_id(prod.id_produto)[0]['val_preco']

            OrderItensGateway().create_order_item(order_itens)

        
        #ao realizar pedido é necessário criar pagamento
        dados_pagamento = Payment(val_valor=total_value, val_status=0, id_pedido=order_number)
        PaymentUseCase().generate_payment(pay=dados_pagamento)
        

        return order_number       

            
    def update_order_status(self, order: Order) -> Order | None:        

        return OrderGateway().update_order(pedido=order.model_dump())

    
    def get_all_orders_ordered(self)  -> List | None:        
        order_data =  OrderGateway().get_all_orders()

        #ordenando valores
        custom_status_order = {'Pronto': 1, 'Em Preparação': 2, 'Recebido': 3, 'Finalizado': 4, 'Aguardando Pagamento':5}

        sorted_data = sorted(order_data, key=lambda x: (custom_status_order.get(x['ds_status'], float('inf')), x['id_pedido']))

        #filtrando finalizados
        filtered_data = [item for item in sorted_data if item['ds_status'] != 'Finalizado']

        #filtrando pagamento (não é pedido)
        filtered_data = [item for item in filtered_data if item['ds_status'] != 'Aguardando Pagamento']

                
        if filtered_data:            
            return filtered_data        
        else:      
            raise HTTPException(status_code=404, detail="Item not found")        
          
    

    