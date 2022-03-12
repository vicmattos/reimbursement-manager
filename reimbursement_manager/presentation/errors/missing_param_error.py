class MissingParamError(Exception):
    def __init__(self, param_name: str):
        self.message = f"Missing param: {param_name}"
        super().__init__(self.message)
