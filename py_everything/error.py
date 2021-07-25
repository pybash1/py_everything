class pycacheNotFoundError(Exception):
    def __init__(self):
        self.msg = "__pycache__ folder was not found!"
        super().__init__(self.msg)

class installModulesFailedError(Exception):
    def __init__(self):
        self.msg = "The modules could not be installed! Some error occurred!"
        super().__init__(self.msg)

class startAppFailedError(Exception):
    def __init__(self):
        self.msg = "App could not be started due to some problem"
        super().__init__(self.msg)

class InvalidKeyListError(Exception):
    def __init__(self):
        self.msg: str = "Given Key List is Invaild"
        super().__init__(self.msg)

class InvalidSymbolKeyError(Exception):
    def __init__(self):
        self.msg: str = "The given Symbol Key is Invalid"
        super().__init__(self.msg)

class InvalidOperationPerformedError(Exception):
    def __init__(self):
        self.msg: str = "The operation was performed on a local path where the operation was  for web paths or vice versa"
        super().__init__(self.msg)

class UnknownPathTypeError(Exception):
    def __init__(self):
        self.msg: str = "Provided path did not match any available types - web, and local"
        super().__init__(self.msg)

class UnknownDivisionTypeError(Exception):
    def __init__(self, type: str):
        self.msg: str = f'Unknown division type \'{type}\''
        super().__init__(self.msg)
