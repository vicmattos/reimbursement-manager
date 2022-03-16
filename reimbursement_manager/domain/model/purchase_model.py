from dataclasses import dataclass
from datetime import date
from decimal import Decimal


@dataclass
class PurchaseModel():
    id: str
    amount: Decimal
    currency: str
    date: date
