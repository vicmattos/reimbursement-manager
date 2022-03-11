
from reimbursement_manager.presentation.protocols.http import HttpResponse, HttpRequest

class AddPurchaseController():
    def handle(self, request: HttpRequest) -> HttpResponse:

        if request.body.get('amount') is None:
            return HttpResponse(
                status_code = 400,
                body = {
                    'message': "Missing param: amount"
                }
            )

        if request.body.get('currency') is None:
            return HttpResponse(
                status_code = 400,
                body = {
                    'message': "Missing param: currency"
                }
            )
