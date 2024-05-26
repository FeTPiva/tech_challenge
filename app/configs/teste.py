from db_info import conf_db
import json

def seleciona_tudo(cpf):
    objeto = conf_db()
    connection = objeto.con_mysql()

    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM cliente where ds_cpf = {cpf}")
    myresult = cursor.fetchall()

    print(json.dumps(myresult))

    return myresult

seleciona_tudo(123)