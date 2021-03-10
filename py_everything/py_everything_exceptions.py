class pycacheNotFoundError(Exception):
    def __init__(self, msg):
        self.msg = msg
        super().__init__(self.msg)

class installModulesFailedError(Exception):
    def __init__(self):
        self.msg = "The modules could not be installed! Some error occurred!"
        super().__init__(self.msg)
