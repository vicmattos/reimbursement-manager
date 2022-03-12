from abc import ABC, abstractmethod

from reimbursement_manager.presentation.protocols.http import HttpRequest, HttpResponse


class Controller(ABC):

    @abstractmethod
    def handle(self, http_request: HttpRequest) -> HttpResponse:
        raise NotImplementedError()
