from datetime import date
from decimal import Decimal


class PurchaseModel():

    def __init__(self, id, amount, currency, date):  # pragma: no cover
        self._id = id
        self._amount = amount
        self._currency = currency
        self._date = date

    @property
    def id(self):
        return self._id  # pragma: no cover

    @property
    def amount(self) -> Decimal:
        return self._amount  # pragma: no cover

    @property
    def currency(self) -> str:
        return self._currency  # pragma: no cover

    @property
    def date(self) -> date:
        return self._date  # pragma: no cover
