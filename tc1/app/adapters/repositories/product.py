from datetime import datetime


from app.domain.models.product import Product
from app.domain.ports.product import ProductPort
from app.configs.db_info import conf_db


class ProductRepository(ProductPort):

    def __init__(self):
        self.connection = conf_db().con_mysql()


    def get_all_products(self)  -> Product | None:
        cursor = self.connection.cursor()
        cursor.execute(f"SELECT * FROM produto")
        myresult = cursor.fetchall()

        fields = [field_md[0] for field_md in cursor.description]
        result = [dict(zip(fields,row)) for row in myresult]

        if result:
            return result
        return None
    
    
    def get_product_by_id(self, id_produto: int) -> Product | None:       
         
        cursor = self.connection.cursor()

        cursor.execute(f"SELECT * FROM produto where id_produto = {id_produto}")

        myresult = cursor.fetchone()

        fields = [field_md[0] for field_md in cursor.description]
        result = dict(zip(fields, myresult))

        if result:
            return result
        return None
    
    
    def get_product_by_category(self, id_categoria: int) -> Product | None:       
        
        cursor = self.connection.cursor()

        cursor.execute(f"SELECT * FROM produto where id_categoria = {id_categoria}" )

        myresult = cursor.fetchall()
        
        fields = [field_md[0] for field_md in cursor.description]
        result = [dict(zip(fields,row)) for row in myresult]

        if result:
            return result
        return None
    
    
    def create_product(self, produto: Product) -> int:
        ds_nome = produto.ds_nome
        id_categoria = produto.id_categoria
        val_preco = produto.val_preco

        cursor = self.connection.cursor()

        query = "INSERT INTO produto ( ds_nome, id_categoria, val_preco, dt_atualizacao ) VALUES (%s, %s, %s, CURRENT_TIMESTAMP())"
        values =  (ds_nome, id_categoria, val_preco)
        
        cursor.execute(query, values)
        self.connection.commit()

        return cursor.lastrowid
        
   
    def update_product(self, produto: Product) -> Product | None:
        id_produto = produto.id_produto
        ds_nome = produto.ds_nome
        id_categoria = produto.id_categoria
        val_preco = produto.val_preco

        cursor = self.connection.cursor()

        query = """update produto 
        set ds_nome  = %s, id_categoria = %s, val_preco =%s, dt_atualizacao = CURRENT_TIMESTAMP() 
        where id_produto = %s"""
        values = (ds_nome, id_categoria, val_preco, id_produto)
        cursor.execute(query, values)
        self.connection.commit()

        return None    

    
    def delete_product(self, id_produto: int):

        cursor = self.connection.cursor()

        cursor.execute(f"delete from produto where id_produto = {id_produto}" )
        self.connection.commit()
    
        return None

    

    