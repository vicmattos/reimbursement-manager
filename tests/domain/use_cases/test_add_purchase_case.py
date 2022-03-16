from copy import deepcopy
from datetime import date
from decimal import Decimal

import pytest

from reimbursement_manager.domain.use_cases.add_purchase_case import AddPurchaseModel


@pytest.fixture
def sut():
    amount = Decimal(10.00)
    currency = 'BRL'
    purchase_date = date.today()
    return AddPurchaseModel(amount, currency, purchase_date)


def test_result_true_comparing_with_correct_values(sut):
    other = deepcopy(sut)
    # verify that are different objects
    assert id(sut) != id(other)
    assert sut == other
