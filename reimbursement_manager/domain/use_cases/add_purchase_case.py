from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import date
from decimal import Decimal

from reimbursement_manager.domain.model.purchase_model import PurchaseModel


@dataclass
class AddPurchaseModel():
    amount: Decimal
    currency: str
    date: date


class AddPurchase(ABC):

    @abstractmethod
    def add(self, add_purchase_model: AddPurchaseModel) -> PurchaseModel:
        raise NotImplementedError()  # pragma: no cover
