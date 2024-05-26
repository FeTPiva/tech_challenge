from abc import ABC, abstractmethod
from app.domain.models.client import Client


class ClientPort(ABC):

    @abstractmethod
    def get_client_by_cpf(self, ds_cpf: int) -> Client | None:
        pass

    @abstractmethod
    def get_all_clients(self) -> Client | None:
        pass

    @abstractmethod
    def create_client(self, client: Client) -> Client:
        pass
'''
    @abstractmethod
    def update_client(self, client: Client) -> Client | None:
        pass

    @abstractmethod
    def delete_client(self, ds_cpf: int):
        pass'''