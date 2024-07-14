
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Order(Base):
    __tablename__ = "pedido"

    id_pedido = Column(Integer, primary_key=True)
    dt_pedido = Column(TIMESTAMP, default=datetime.now())
    dt_entrega = Column(TIMESTAMP, default=datetime.now())
    ds_status = Column(String)
    id_cliente = Column(Integer)


class OrderItens(Base):
    __tablename__ = "itens_pedido"

    id_itens_pedido = Column(Integer, primary_key=True)
    id_pedido = Column(Integer)
    id_produto = Column(Integer)

