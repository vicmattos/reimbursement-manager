from dataclasses import dataclass
from typing import Optional


@dataclass
class HttpResponse:
    status_code: int
    body: Optional[dict] = None


class HttpRequest():

    def __init__(self, body: dict = None):
        self._body = body

    @property
    def body(self):
        return self._body
