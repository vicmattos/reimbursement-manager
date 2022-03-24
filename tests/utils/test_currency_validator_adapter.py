
import pytest

from reimbursement_manager.utils.currency_validator_adapter import CurrencyValidatorAdapter


@pytest.fixture
def sut():
    return CurrencyValidatorAdapter()


def test_return_false_if_invalid_currency(sut):
    is_valid: bool = sut.is_valid("invalid_currency")
    assert is_valid is False
