
from iso4217 import Currency  # type: ignore

from reimbursement_manager.presentation.protocols.currency_validator import CurrencyValidator


class CurrencyValidatorAdapter(CurrencyValidator):

    def is_valid(self, currency: str) -> bool:
        try:
            Currency(currency)
            return True
        except Exception:
            return False
