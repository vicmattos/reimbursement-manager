from datetime import date
from decimal import Decimal
from typing import Dict, List, Tuple

from reimbursement_manager.domain.use_cases.add_purchase_case import AddPurchase, AddPurchaseModel
from reimbursement_manager.presentation.errors import InvalidParamError, MissingParamError
from reimbursement_manager.presentation.protocols import Controller, CurrencyValidator, HttpRequest, HttpResponse
from reimbursement_manager.presentation.helpers.http_helper import (  # noqa: I100
    internal_error_response, invalid_request_response, success_response
)


class AddPurchaseController(Controller):

    def __init__(self, add_purchase: AddPurchase, currency_validator: CurrencyValidator) -> None:
        self._add_purchase = add_purchase
        self._currency_validator = currency_validator

    def handle(self, request: HttpRequest) -> HttpResponse:
        try:
            self._validate_required_fields(['amount', 'currency', 'date'], request.body)
            amount, currency, pdate = self._extract_body_values(request.body)

            self._validate_amount(amount)
            self._validate_currency(currency)

            self._add(amount, currency, pdate)
            response = success_response()

        except (MissingParamError, InvalidParamError) as err:
            response = invalid_request_response(message=err.message)
        except Exception:
            response = internal_error_response()

        return response


    def _validate_required_fields(self, required_fields: List[str], body: Dict) -> None:  # noqa: E303
        for required_field in required_fields:
            field_value = body.get(required_field, None)  # type: ignore
            if field_value is None:
                raise MissingParamError(param_name=required_field)


    def _extract_body_values(self, request_body: Dict) -> Tuple[Decimal, str, date]:  # noqa: E303
        amount: Decimal = request_body.get('amount')  # type: ignore
        currency: str = request_body.get('currency')  # type: ignore
        date: date = request_body.get('date')  # type: ignore
        return amount, currency, date


    def _validate_amount(self, amount: Decimal) -> None:  # noqa: E303
        if amount.is_zero() or amount.is_signed():
            raise InvalidParamError(param_name='amount')


    def _validate_currency(self, currency: str) -> None:  # noqa: E303
        is_valid = self._currency_validator.is_valid(currency)
        if not is_valid:
            raise InvalidParamError(param_name='currency')


    def _add(self, amount: Decimal, currency: str, pdate: date) -> None:  # noqa: E303
        model = AddPurchaseModel(amount, currency, pdate)
        self._add_purchase.add(model)
