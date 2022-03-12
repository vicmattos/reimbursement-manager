
from reimbursement_manager.presentation.helpers.http_helper import invalid_request_response
from reimbursement_manager.presentation.protocols.http import HttpResponse, HttpRequest
from reimbursement_manager.presentation.protocols.controller import Controller
from reimbursement_manager.presentation.protocols.currency_validator import CurrencyValidator
from reimbursement_manager.presentation.errors import MissingParamError

class AddPurchaseController(Controller):

    def __init__(self, currency_validator: CurrencyValidator):
        self._currency_validator = currency_validator

    def handle(self, request: HttpRequest) -> HttpResponse:

        try:
            for required_field in ['amount', 'currency', 'date']:
                field_value = request.body.get(required_field, None)
                if field_value is None:
                    raise MissingParamError(param_name=required_field)

            currency = request.body.get('currency')
            is_valid = self._currency_validator.is_valid(currency)
            if not is_valid:
                raise Exception('Invalid param: currency')

        except (MissingParamError, Exception) as err:
            response = invalid_request_response(message=str(err))

        return response
