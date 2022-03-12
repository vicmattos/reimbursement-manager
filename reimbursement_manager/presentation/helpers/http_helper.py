from http import HTTPStatus

from reimbursement_manager.presentation.protocols.http import HttpResponse


def invalid_request_response(message: str) -> HttpResponse:
    body = {"message": message}
    return HttpResponse(status_code=HTTPStatus.BAD_REQUEST.value, body=body)
