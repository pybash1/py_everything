import os
import re
import error # type: ignore
import webbrowser
import requests

isUrl = re.compile(r'((\S*)?:\/\/(.)?)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.?[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/=]*)')
isLocal = re.compile(r'^(.*/)([^/]*)$')

class Path:
    def __init__(self, path: str):
        self.path = path
        
        if isUrl.match(self.path):
            self.type = 'web'
        elif isLocal.match(self.path):
            self.type = 'local'
        else:
            raise error.UnknownPathTypeError()
            
    def getType(self):
        return self.type
    
    def getRawPath(self):
        return self.path
    
    def getRealPath(self):
        if self.type == 'web':
            raise error.InvalidOperationPerformedError()
        else:
            return os.path.realpath(self.path)
            
    def isFile(self):
        if self.type == 'web':
            raise error.InvalidOperationPerformedError()
        else:
            return os.path.isfile(self.path)
        
    def isDir(self):
        if self.type == 'web':
            raise error.InvalidOperationPerformedError()
        else:
            return os.path.isdir(self.path)
        
    def getRelativePath(self):
        if self.type == 'web':
            raise error.InvalidOperationPerformedError()
        else:
            return os.path.relpath(self.path)
        
    def getLastAccessTime(self):
        if self.type == 'web':
            raise error.InvalidOperationPerformedError()
        else:
            return os.path.getatime(self.path)
        
    def getLastModifiedTime(self):
        if self.type == 'web':
            raise error.InvalidOperationPerformedError()
        else:
            return os.path.getmtime(self.path)

    def openInBrowser(self):
        if self.type == 'local':
            raise error.InvalidOperationPerformedError()
        else:
            webbrowser.open(self.path)
        
    def getRequest(self):
        if self.type == 'local':
            raise error.InvalidOperationPerformedError()
        else:
            res = requests.get(self.path)
            
            return res
            
    def getRequestStatusCode(self):
        if self.type == 'local':
            raise error.InvalidOperationPerformedError()
        else:
            res = requests.get(self.path)
            
            return res.status_code
