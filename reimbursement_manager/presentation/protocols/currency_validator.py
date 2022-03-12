from abc import ABC, abstractmethod


class CurrencyValidator(ABC):

    @abstractmethod
    def is_valid(self, currency: str) -> bool:
        raise NotImplementedError() # pragma: no cover
