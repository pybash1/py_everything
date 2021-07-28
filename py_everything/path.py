import os
import re
from . import error # type: ignore
import webbrowser
import requests

isUrl = re.compile(r'((\S*)?:\/\/(.)?)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.?[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&\/=]*)')
isLocal = re.compile(r'^(.*/)([^/]*)$')

class Path:
    """Class that has useful methods for paths"""
    def __init__(self, path: str):
        self.path: str = path
        
        if isUrl.match(self.path):
            self.type = 'web'
        elif isLocal.match(self.path):
            self.type = 'local'
        else:
            raise error.UnknownPathTypeError()
            
    def getType(self):
        """Returns tpye of path"""
        return self.type
    
    def getRawPath(self):
        """Returns raw input path"""
        return self.path
    
    def getRealPath(self):
        """Returns full path formatted correctly"""
        if self.type == 'web':
            raise error.InvalidOperationPerformedError()
        return os.path.realpath(self.path)
    
    def isFile(self):
        """Returns if path is a file or not"""
        if self.type == 'web':
            raise error.InvalidOperationPerformedError()
        return os.path.isfile(self.path)
        
    def isDir(self):
        """Returns if path is a directory or not"""
        if self.type == 'web':
            raise error.InvalidOperationPerformedError()
        return os.path.isdir(self.path)
        
    def getRelativePath(self):
        """Returns path relative to current directory"""
        if self.type == 'web':
            raise error.InvalidOperationPerformedError()
        return os.path.relpath(self.path)
        
    def getLastAccessTime(self):
        """Returns time when path was last accessed"""
        if self.type == 'web':
            raise error.InvalidOperationPerformedError()
        return os.path.getatime(self.path)
        
    def getLastModifiedTime(self):
        """Returns time when path was last modified"""
        if self.type == 'web':
            raise error.InvalidOperationPerformedError()
        return os.path.getmtime(self.path)

    def openInBrowser(self):
        """Open path in browser"""
        if self.type == 'local':
            raise error.InvalidOperationPerformedError()
        webbrowser.open(self.path)
        
    def getRequest(self):
        """Returns data returned by path on get request"""
        if self.type == 'local':
            raise error.InvalidOperationPerformedError()
        res = requests.get(self.path)

        return res
    
    def getRequestStatusCode(self):
        """Returns status code for request to path"""
        if self.type == 'local':
            raise error.InvalidOperationPerformedError()
        res = requests.get(self.path)

        return res.status_code
