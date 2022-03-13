from typing import List

from reimbursement_manager.presentation.helpers.http_helper import invalid_request_response, internal_error_response
from reimbursement_manager.presentation.protocols import HttpResponse, HttpRequest, Controller, CurrencyValidator
from reimbursement_manager.presentation.errors import MissingParamError, InvalidParamError

class AddPurchaseController(Controller):

    def __init__(self, currency_validator: CurrencyValidator):
        self._currency_validator = currency_validator

    def handle(self, request: HttpRequest) -> HttpResponse:
        try:
            self._validate_required_fields(request.body, ['amount', 'currency', 'date'])
            self._validate_amount(request.body.get('amount'))
            self._validate_currency(request.body.get('currency'))

        except (MissingParamError, InvalidParamError) as err:
            response = invalid_request_response(message=err.message)
        except Exception:
            response = internal_error_response()

        return response


    def _validate_required_fields(self, body: dict, required_fields: List[str]) -> None:
        for required_field in required_fields:
            field_value = body.get(required_field, None)
            if field_value is None:
                raise MissingParamError(param_name=required_field)


    def _validate_amount(self, amount: int) -> None:
        if amount <= 0:
            raise InvalidParamError(param_name='amount')


    def _validate_currency(self, currency: str) -> None:
        is_valid = self._currency_validator.is_valid(currency)
        if not is_valid:
            raise InvalidParamError(param_name='currency')
