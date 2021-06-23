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
        self.msg = "Given Key List is Invaild"
        super().__init__(self.msg)

class InvalidSymbolKeyError(Exception):
    def __init__(self):
        self.msg = "The given Symbol Key is Invalid"
        super().__init__(self.msg)
        
def TypeError(currentType):
    raise TypeError(f'Write Content Must Be Str Not {currentType}')

class InvalidOperationPerformedError(Exception):
    def __init__(self):
        self.msg = "Operation performed is either invalid on the type of the object or the operation is invalid"
        super().__init__(self.msg)

class UnknownPathTypeError(Exception):
    def __init__(self):
        self.msg = "Provided path did not match any available types - web, and local"
