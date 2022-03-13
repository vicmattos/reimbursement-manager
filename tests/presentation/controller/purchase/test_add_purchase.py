
from decimal import Decimal
from datetime import date

import pytest

from reimbursement_manager.presentation.controller.purchase import AddPurchaseController
from reimbursement_manager.presentation.protocols import HttpResponse, HttpRequest, CurrencyValidator


@pytest.fixture
def sut(currency_validator_stub):
    return AddPurchaseController(currency_validator_stub)


@pytest.fixture
def http_request():
    return HttpRequest(
        body = dict(
            amount = Decimal(10.00),
            currency = "BRL",
            date = date.today()
        )
    )


@pytest.fixture
def currency_validator_stub():
    class CurrencyValidatorStub(CurrencyValidator):
        def is_valid(self, currency: str) -> bool:
            return True
    return CurrencyValidatorStub()


def test_return_400_if_no_amount_is_provided(sut, http_request):
    http_request.body.pop('amount', None)
    http_response: HttpResponse = sut.handle(http_request)
    assert http_response.status_code == 400
    assert http_response.body.get('message') == "Missing param: amount"


def test_return_400_if_no_currency_is_provided(sut, http_request):
    http_request.body.pop('currency', None)
    http_response: HttpResponse = sut.handle(http_request)
    assert http_response.status_code == 400
    assert http_response.body.get('message') == "Missing param: currency"


def test_return_400_if_no_date_is_provided(sut, http_request):
    http_request.body.pop('date', None)
    http_response: HttpResponse = sut.handle(http_request)
    assert http_response.status_code == 400
    assert http_response.body.get('message') == "Missing param: date"


def test_return_400_if_negative_amount_is_provided(sut, http_request, mocker):
    # Change value in http_request.body['amount'] to negative
    mocker.patch.dict(http_request.body, {'amount': -1})
    http_response: HttpResponse = sut.handle(http_request)
    assert http_response.status_code == 400
    assert http_response.body.get('message') == "Invalid param: amount"


def test_return_400_if_zero_amount_is_provided(sut, http_request, mocker):
    # Change value in http_request.body['amount'] to negative
    mocker.patch.dict(http_request.body, {'amount': 0})
    http_response: HttpResponse = sut.handle(http_request)
    assert http_response.status_code == 400
    assert http_response.body.get('message') == "Invalid param: amount"


def test_return_400_if_invalid_currency_is_provided(sut, http_request, currency_validator_stub, mocker):
    # Make `currency_validator.is_valid` return False
    mocker.patch.object(currency_validator_stub, "is_valid", return_value=False)
    http_response: HttpResponse = sut.handle(http_request)
    assert http_response.status_code == 400
    assert http_response.body.get('message') == "Invalid param: currency"


def test_ensure_currency_validator_call_for_invalid_currency(sut, http_request, currency_validator_stub, mocker):
    tested_currency_value = "Some currency"
    # Make `currency_validator.is_valid` return False
    mocker.patch.object(currency_validator_stub, "is_valid", return_value=False)
    # Monitor method currency_validator_stub.is_valid
    spy = mocker.spy(currency_validator_stub, "is_valid")
    # Change value in http_request.body['currency'] to specified
    mocker.patch.dict(http_request.body, {'currency': tested_currency_value})
    sut.handle(http_request)
    spy.assert_called_once_with(tested_currency_value)


def test_return_500_if_CurrencyValidator_raises_error(sut, http_request, currency_validator_stub, mocker):
    # Make `currency_validator.is_valid` raises Exception
    mocker.patch.object(currency_validator_stub, "is_valid", side_effect=Exception)
    http_response: HttpResponse = sut.handle(http_request)
    assert http_response.status_code == 500
    assert http_response.body.get('message') == "Internal Server Error"
