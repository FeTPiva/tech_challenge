from abc import ABC, abstractmethod
from app.domain.models.order import Order


class OrderPort(ABC):

    @abstractmethod
    def get_all_orders(self) -> Order | None:
        pass
    
    @abstractmethod
    def get_order_by_id(self, id_pedido) -> Order |None:
        pass

    @abstractmethod
    def create_order(self, pedido: Order) -> int:
        pass

    @abstractmethod
    def update_order(self, pedido: Order) -> None:
        pass

    @abstractmethod
    def get_all_orders_details(self) -> Order | None:
        pass

    @abstractmethod
    def get_order_by_id_details(self, id_pedido) -> Order |None:
        pass
