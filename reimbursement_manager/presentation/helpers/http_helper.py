from http import HTTPStatus

from reimbursement_manager.presentation.protocols.http import HttpResponse


def success_response() -> HttpResponse:
    return HttpResponse(status_code=HTTPStatus.OK.value)


def invalid_request_response(message: str) -> HttpResponse:
    body = {"message": message}
    return HttpResponse(status_code=HTTPStatus.BAD_REQUEST.value, body=body)


def internal_error_response(error: str = "Internal Server Error") -> HttpResponse:
    return HttpResponse(
        status_code=HTTPStatus.INTERNAL_SERVER_ERROR.value,
        body={"message": error}
    )
