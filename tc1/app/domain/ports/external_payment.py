from abc import ABC, abstractmethod

class FakePaymentPort(ABC):

    @abstractmethod
    def get_qrcode() -> None:
        pass

    @abstractmethod
    def get_payment_status() -> bool:
        return True
