
from reimbursement_manager.presentation.helpers.http_helper import invalid_request_response
from reimbursement_manager.presentation.protocols.http import HttpResponse, HttpRequest
from reimbursement_manager.presentation.protocols.controller import Controller
from reimbursement_manager.presentation.errors import MissingParamError

class AddPurchaseController(Controller):
    def handle(self, request: HttpRequest) -> HttpResponse:

        try:
            for required_field in ['amount', 'currency', 'date']:
                field_value = request.body.get(required_field, None)
                if field_value is None:
                    raise MissingParamError(param_name=required_field)

        except (MissingParamError) as err:
            response = invalid_request_response(message=err.message)

        return response
