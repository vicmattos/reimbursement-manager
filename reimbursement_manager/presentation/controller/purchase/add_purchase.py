from typing import List

from reimbursement_manager.presentation.helpers.http_helper import invalid_request_response, internal_error_response, success_response
from reimbursement_manager.presentation.protocols import HttpResponse, HttpRequest, Controller, CurrencyValidator
from reimbursement_manager.presentation.errors import MissingParamError, InvalidParamError
from reimbursement_manager.domain.use_cases.add_purchase import AddPurchase

class AddPurchaseController(Controller):

    def __init__(self, add_purchase: AddPurchase, currency_validator: CurrencyValidator):
        self._add_purchase = add_purchase
        self._currency_validator = currency_validator

    def handle(self, request: HttpRequest) -> HttpResponse:
        try:
            self._validate_required_fields(['amount', 'currency', 'date'], request.body)
            self._validate_amount(request.body.get('amount'))
            self._validate_currency(request.body.get('currency'))

            self._add_purchase.add(
                amount=request.body.get('amount'),
                currency=request.body.get('currency'),
                date=request.body.get('date')
            )

            response = success_response()

        except (MissingParamError, InvalidParamError) as err:
            response = invalid_request_response(message=err.message)
        except Exception:
            response = internal_error_response()

        return response


    def _validate_required_fields(self, required_fields: List[str], body: dict) -> None:
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
