
from typing import Any

class AddPurchaseController():
    def handle(self, request: Any) -> Any:
        if request['body'].get('amount') is None:
            return {
                'status_code': 400,
                'body': "Missing param: amount"
            }
        if request['body'].get('currency') is None:
            return {
                'status_code': 400,
                'body': "Missing param: currency"
            }
