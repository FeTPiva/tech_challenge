from sqlalchemy import Boolean, Column, ForeignKey, Integer, String

from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


class Client(base):
    __tablename__ = "cliente"

    id_cliente = Column(Integer, primary_key=True)
    ds_cpf = Column(String)
    ds_nome = Column(String)
    ds_email = Column(String)



