
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

class mysql_connection:
    #https://github.com/0xTheProDev/fastapi-clean-example/blob/main/repositories/AuthorRepository.py

    def __init__(self):
        self.host="test",
        self.user="root",
        self.passw="password",
        self.db="db"

        self.engine = create_engine(f"mysql+pymysql://{self.username}:{self.passw}@{self.host}/{self.db}?charset=utf8mb4")

        self.SessionLocal = sessionmaker(
            autocommit=False, autoflush=False, bind=self.engine)
        
        #self.EntityMeta = declarative_base()
        self.base = declarative_base().metadata.create_all(bind=self.engine)
        #self.EntityMeta.metadata.create_all(bind=self.engine)


    def get_db_connection(self):
        db = scoped_session(self.SessionLocal)
        try:
            yield db
        finally:
            db.close()


