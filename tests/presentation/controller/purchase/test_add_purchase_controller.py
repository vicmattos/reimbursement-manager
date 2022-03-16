
from datetime import date
from decimal import Decimal

import pytest

from reimbursement_manager.domain.model.purchase_model import PurchaseModel
from reimbursement_manager.domain.use_cases.add_purchase_case import AddPurchase, AddPurchaseModel
from reimbursement_manager.presentation.controller.purchase import AddPurchaseController
from reimbursement_manager.presentation.protocols import CurrencyValidator, HttpRequest, HttpResponse


@pytest.fixture
def sut(dummy_add_purchase, stub_currency_validator):
    return AddPurchaseController(dummy_add_purchase, stub_currency_validator)


@pytest.fixture
def fake_http_request():
    return HttpRequest(
        body=dict(
            amount=Decimal(10.00),
            currency="BRL",
            date=date.today()
        )
    )


@pytest.fixture
def dummy_add_purchase():
    class AddPurchaseDummy(AddPurchase):
        def add(self, add_purchase_model: AddPurchaseModel) -> PurchaseModel:
            pass
    return AddPurchaseDummy()


@pytest.fixture
def fake_add_purchase_model(fake_http_request):
    return AddPurchaseModel(
        amount=fake_http_request.body.get('amount'),
        currency=fake_http_request.body.get('currency'),
        date=fake_http_request.body.get('date'),
    )


@pytest.fixture
def stub_currency_validator():
    class CurrencyValidatorStub(CurrencyValidator):
        def is_valid(self, currency: str) -> bool:
            return True
    return CurrencyValidatorStub()


def test_return_400_if_no_amount_is_provided(sut, fake_http_request):
    fake_http_request.body.pop('amount', None)
    http_response: HttpResponse = sut.handle(fake_http_request)
    assert http_response.status_code == 400
    assert http_response.body.get('message') == "Missing param: amount"


def test_return_400_if_no_currency_is_provided(sut, fake_http_request):
    fake_http_request.body.pop('currency', None)
    http_response: HttpResponse = sut.handle(fake_http_request)
    assert http_response.status_code == 400
    assert http_response.body.get('message') == "Missing param: currency"


def test_return_400_if_no_date_is_provided(sut, fake_http_request):
    fake_http_request.body.pop('date', None)
    http_response: HttpResponse = sut.handle(fake_http_request)
    assert http_response.status_code == 400
    assert http_response.body.get('message') == "Missing param: date"


def test_return_400_if_negative_amount_is_provided(sut, fake_http_request, mocker):
    # Change value in fake_http_request.body['amount'] to negative
    mocker.patch.dict(fake_http_request.body, {'amount': Decimal(-1)})
    http_response: HttpResponse = sut.handle(fake_http_request)
    assert http_response.status_code == 400
    assert http_response.body.get('message') == "Invalid param: amount"


def test_return_400_if_zero_amount_is_provided(sut, fake_http_request, mocker):
    # Change value in fake_http_request.body['amount'] to negative
    mocker.patch.dict(fake_http_request.body, {'amount': Decimal(0)})
    http_response: HttpResponse = sut.handle(fake_http_request)
    assert http_response.status_code == 400
    assert http_response.body.get('message') == "Invalid param: amount"


def test_return_400_if_invalid_currency_is_provided(sut, fake_http_request, stub_currency_validator, mocker):
    # Make `currency_validator.is_valid` return False
    mocker.patch.object(stub_currency_validator, "is_valid", return_value=False)
    http_response: HttpResponse = sut.handle(fake_http_request)
    assert http_response.status_code == 400
    assert http_response.body.get('message') == "Invalid param: currency"


def test_ensure_currency_validator_call_for_invalid_currency(sut, fake_http_request, stub_currency_validator, mocker):
    tested_currency_value = "Some currency"
    # Make `currency_validator.is_valid` return False
    mocker.patch.object(stub_currency_validator, "is_valid", return_value=False)
    # Monitor method stub_currency_validator.is_valid
    spy = mocker.spy(stub_currency_validator, "is_valid")
    # Change value in fake_http_request.body['currency'] to specified
    mocker.patch.dict(fake_http_request.body, {'currency': tested_currency_value})
    sut.handle(fake_http_request)
    spy.assert_called_once_with(tested_currency_value)


def test_return_500_if_CurrencyValidator_raises_error(sut, fake_http_request, stub_currency_validator, mocker):
    # Make `currency_validator.is_valid` raises Exception
    mocker.patch.object(stub_currency_validator, "is_valid", side_effect=Exception)
    http_response: HttpResponse = sut.handle(fake_http_request)
    assert http_response.status_code == 500
    assert http_response.body.get('message') == "Internal Server Error"


def test_call_add_purchase_with_correct_values(sut, fake_http_request, dummy_add_purchase, fake_add_purchase_model, mocker):
    # Monitor method dummy_add_purchase.add
    spy = mocker.spy(dummy_add_purchase, "add")
    sut.handle(fake_http_request)
    spy.assert_called_once_with(fake_add_purchase_model)


def test_return_200_if_correct_values_are_provided(sut, fake_http_request):
    http_response: HttpResponse = sut.handle(fake_http_request)
    assert http_response.status_code == 200
