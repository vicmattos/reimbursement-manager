from dataclasses import dataclass, field
from typing import Optional


@dataclass
class HttpResponse:
    status_code: int
    body: Optional[dict] = None


@dataclass
class HttpRequest:
    body: dict = field(default_factory=dict)
