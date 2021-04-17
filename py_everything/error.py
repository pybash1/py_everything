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
