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

       
    def update_order(self, pedido: dict) -> Order | None:        
        return ConfDB().update_data(table='pedido', data=pedido, filter_field='id_pedido', value=pedido['id_pedido'])
    

    def get_all_orders_details_old(self) -> Order | None:
        cursor = self.connection.cursor()
        cursor.execute("""select p.id_pedido,
                       p.ds_status,
                       p.id_cliente,
                       i.id_produto,
                       pr.ds_nome,
                       pr.val_preco,
                       p.dt_pedido,
                       p.dt_entrega from pedido p 
            left join itens_pedido i on p.id_pedido = i.id_pedido
            left join produto pr on i.id_produto = pr.id_produto""")
        myresult = cursor.fetchall()

        fields = [field_md[0] for field_md in cursor.description]
        result = [dict(zip(fields,row)) for row in myresult]

        if result:
            return result
        return None
    
    

    def get_order_by_id_details_old(self, id_pedido:int) -> None:
                
        cursor = self.connection.cursor()

        cursor.execute(f"""select p.id_pedido, p.ds_status, p.id_cliente,
                       i.id_produto, pr.ds_nome, pr.val_preco, p.dt_pedido,
                       p.dt_entrega 
                       from pedido p
                       left join itens_pedido i on p.id_pedido = i.id_pedido
                       left join produto pr on i.id_produto = pr.id_produto
                       where p.id_pedido = {id_pedido}""")

        myresult = cursor.fetchall()

        fields = [field_md[0] for field_md in cursor.description]
        result = [dict(zip(fields, row)) for row in myresult]

        if result:
            return result
        return None



    def create_order_old(self, order) -> int:

        def create_order_itens(list_itens, id_pedido) -> int:
            cursor = self.connection.cursor()
            
            #inserir os itens escolhidos em itens_pedido
            for item in list_itens:
                
                item_query = "INSERT INTO itens_pedido (id_pedido, id_produto) VALUES  (%s, %s)"
                vals = (id_pedido, item)
                cursor.execute(item_query,vals)
                
            self.connection.commit()

            return cursor.lastrowid


        #para criar sempre vai ser o primeiro status
        ds_status = 'Recebido'
        id_cliente = order.id_cliente
        list_itens = order.list_itens

        
        cursor = self.connection.cursor()
        
        query = "INSERT INTO pedido ( id_cliente, dt_pedido, ds_status ) VALUES (%s, CURRENT_TIMESTAMP(), %s)"
        values =  (id_cliente, ds_status)
        
        cursor.execute(query, values)
        self.connection.commit()

        id_pedido = cursor.lastrowid
        print(order)  
        print(id_pedido)

        create_order_itens(list_itens, id_pedido)

        return id_pedido    

            

    def update_order_old(self, pedido: Order) -> Order | None:
        id_pedido = pedido.id_pedido
        id_cliente = pedido.id_cliente
        dt_pedido = pedido.dt_pedido
        dt_entrega = pedido.dt_entrega
        ds_status = pedido.ds_status

        cursor = self.connection.cursor()

        query = """update pedido 
        set dt_pedido = %s, dt_entrega =%s, ds_status = %s 
        where id_pedido = %s"""
        values = (dt_pedido, dt_entrega, ds_status)
        cursor.execute(query, values)
        self.connection.commit()

        return None    
