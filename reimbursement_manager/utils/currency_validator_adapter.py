
from reimbursement_manager.presentation.protocols.currency_validator import CurrencyValidator


class CurrencyValidatorAdapter(CurrencyValidator):

    def is_valid(self, currency: str) -> bool:
        return False
