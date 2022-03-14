from datetime import date
from decimal import Decimal
from abc import ABC, abstractmethod

from reimbursement_manager.domain.model.purchase import PurchaseModel

class AddPurchaseModel():

    def __init__(self, amount, currency, date):
        self._amount = amount
        self._currency = currency
        self._date = date

    @property
    def amount(self) -> Decimal:
        return self._amount # pragma: no cover

    @property
    def currency(self) -> str:
        return self._currency # pragma: no cover

    @property
    def date(self) -> date:
        return self._date # pragma: no cover

    def __eq__(self, other):
        if not isinstance(other, AddPurchaseModel):
            return False

        same_amount = self._amount == other._amount
        same_currency = self._currency == other._currency
        same_date = self._date == other._date

        return True if (same_amount and same_currency and same_date) else False


class AddPurchase(ABC):

    @abstractmethod
    def add(self, add_purchase_model: AddPurchaseModel) -> PurchaseModel:
        raise NotImplementedError() # pragma: no cover
