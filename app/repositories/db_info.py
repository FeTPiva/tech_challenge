import abc
from mysql.connector import abstracts
from typing import List, Dict, Any


class ConfDBRepository(abc.ABC):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def con_mysql(self) -> abstracts.MySQLConnectionAbstract:
        pass

    @abc.abstractmethod
    def select_all_data(self) -> List:
        pass

    @abc.abstractmethod
    def select_with_filter(self) -> List:
        pass

    @abc.abstractmethod
    def insert_data(self) -> int | None:
        pass

    @abc.abstractmethod
    def delete_data(self) -> None:
        pass
    
    @abc.abstractmethod
    def update_data(Self) -> None:
        pass


    