from abc import ABC, abstractmethod
from app.domain.models.product import Product


class ProductPort(ABC):

    @abstractmethod
    def get_product_by_category(self, id_categoria: int):
        pass

    @abstractmethod
    def get_all_products(self) -> Product | None:
        pass

    @abstractmethod
    def create_product(self, produto: Product) -> Product:
        pass

    @abstractmethod
    def update_product(self, produto: Product) -> Product | None:
        pass

    @abstractmethod
    def delete_product(self, id_produto: int):
        pass