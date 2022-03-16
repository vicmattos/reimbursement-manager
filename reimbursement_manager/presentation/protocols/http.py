from typing import Optional


class HttpResponse():

    def __init__(self, status_code: int, body: Optional[dict]):
        self._status_code = status_code
        self._body = body

    @property
    def status_code(self) -> int:
        return self._status_code

    @property
    def body(self) -> Optional[dict]:
        return self._body


class HttpRequest():

    def __init__(self, body: dict = None):
        self._body = body

    @property
    def body(self):
        return self._body
