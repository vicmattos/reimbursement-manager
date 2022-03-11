
from decimal import Decimal
from datetime import date

from reimbursement_manager.presentation.controller.purchase import AddPurchaseController
from reimbursement_manager.presentation.protocols.http import HttpResponse, HttpRequest

def test_return_400_if_no_amount_is_provided():
    sut = AddPurchaseController()
    http_request = HttpRequest(
        body = dict(
            # amount = Decimal(10.00),
            currency = "BRL",
            date = date.today()
        )
    )
    http_response: HttpResponse = sut.handle(http_request)
    assert http_response.status_code == 400
    assert http_response.body.get('message') == "Missing param: amount"

def test_return_400_if_no_currency_is_provided():
    sut = AddPurchaseController()
    http_request = HttpRequest(
        body = dict(
            amount = Decimal(10.00),
            # currency = "BRL",
            date = date.today()
        )
    )
    http_response: HttpResponse = sut.handle(http_request)
    assert http_response.status_code == 400
    assert http_response.body.get('message') == "Missing param: currency"
