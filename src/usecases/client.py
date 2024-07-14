
from gateways.client import ClientGateway



class ClientUseCase:
    def __init__(self) -> None:
        self.client_gateway = ClientGateway()
        pass

    def get_all_clients(self):
        try:
            return self.client_gateway.get_all_clients()
        except Exception as e:
            print(e)

        
        

