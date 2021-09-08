class pycacheNotFoundError(Exception):
    """Error raised if __pycache__ folder is not found"""

    def __init__(self):
        self.msg = "__pycache__ folder was not found!"
        super().__init__(self.msg)


class installModulesFailedError(Exception):
    """Exception raised if installing modules fails"""

    def __init__(self):
        self.msg = "The modules could not be installed! Some error occurred!"
        super().__init__(self.msg)


class startAppFailedError(Exception):
    """Exception raised if starting executable fails."""

    def __init__(self):
        self.msg = "App could not be started due to some problem"
        super().__init__(self.msg)


class InvalidKeyListError(Exception):
    """Exception raised if key list is invalid"""

    def __init__(self):
        self.msg: str = "Given Key List is Invaild"
        super().__init__(self.msg)


class InvalidSymbolKeyError(Exception):
    """Exception raised if symbol key is invalid"""

    def __init__(self):
        self.msg: str = "The given Symbol Key is Invalid"
        super().__init__(self.msg)


class InvalidOperationPerformedError(Exception):
    """Exception raised when an operation performed is invalid"""

    def __init__(self):
        self.msg: str = "The operation was performed on a local path where the operation was  for web paths or vice versa"
        super().__init__(self.msg)


class UnknownPathTypeError(Exception):
    """Exception raised if path type is unknown"""

    def __init__(self):
        self.msg: str = (
            "Provided path did not match any available types - web, and local"
        )
        super().__init__(self.msg)


class UnknownDivisionTypeError(Exception):
    """Exception raised if division type is unknown"""

    def __init__(self, type: str):
        self.msg: str = f"Unknown division type '{type}'"
        super().__init__(self.msg)
