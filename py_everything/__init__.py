import os
import subprocess
import shutil
from . import error

# Variables for the package
__author__ = "PyBash"
__version__ = "v2.0.0"

def helloWorld():
    string = 'Hello, World!'
    print(string)


def printNoNewline(*args):
    for arg in args:
        print(arg, end=" ")


def clearPycache(path):
    if shutil.rmtree(os.path.join(path, "__pycache__")):
        return True
    else:
        raise error.pycacheNotFoundError()


def installModules(*args):
    for module in args:
        command = "python -m pip install {}".format(module)
        if subprocess.run(command):
            return True
        else:
            raise error.installModulesFailedError()

def alphabet():
    theAlphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return theAlphabet

def alphabetCaps():
    theAlphabetCaps = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return theAlphabetCaps

def alphabetStr():
    theAlphabet = 'abcdefghijklmnopqrstwxyz'
    return theAlphabet

def alphabetCapsStr():
    theAlphabetCaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return theAlphabetCaps

def nums():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    return nums

def syms():
    symbols = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','\\',':',';','"','\'','<',',','>','.','?','/']
    return symbols
