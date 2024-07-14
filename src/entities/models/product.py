
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Float, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Product(Base):
    __tablename__ = "produto"

    id_produto = Column(Integer, primary_key=True)
    ds_nome = Column(String)
    id_categoria = Column(Integer)
    val_preco = Column(Float)
    dt_atualizacao = Column(TIMESTAMP, default=datetime.now())


class ProductCategories(Base):
    __tablename__ = "categoria_produtos"

    id_categoria = Column(Integer, primary_key=True)
    ds_nome = Column(String)


