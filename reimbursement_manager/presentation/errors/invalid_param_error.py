class InvalidParamError(Exception):
    def __init__(self, param_name: str) -> None:
        self.message = f"Invalid param: {param_name}"
        super().__init__(self.message)
