
from reimbursement_manager.presentation.helpers.http_helper import invalid_request_response
from reimbursement_manager.presentation.protocols.http import HttpResponse, HttpRequest

class AddPurchaseController():
    def handle(self, request: HttpRequest) -> HttpResponse:

        if request.body.get('amount') is None:
            response: HttpResponse = invalid_request_response(message="Missing param: amount")

        if request.body.get('currency') is None:
            response: HttpResponse = invalid_request_response(message="Missing param: currency")

        if request.body.get('date') is None:
            response: HttpResponse = invalid_request_response(message="Missing param: date")

        return response
