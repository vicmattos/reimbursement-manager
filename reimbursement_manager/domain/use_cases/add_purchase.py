from datetime import date
from decimal import Decimal
from abc import ABC, abstractmethod

class AddPurchase(ABC):

    @abstractmethod
    def add(self, amount: Decimal, currency: str, date: date) -> None:
        raise NotImplementedError()
