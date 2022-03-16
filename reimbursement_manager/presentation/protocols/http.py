from dataclasses import dataclass
from typing import Optional


@dataclass
class HttpResponse:
    status_code: int
    body: Optional[dict] = None


@dataclass
class HttpRequest:
    body: Optional[dict] = None
