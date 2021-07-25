import os
import subprocess
import shutil
from . import error
from typing import List

# Variables for the package
__author__: str = "PyBash"
__version__: str = "v2.0.0"

def helloWorld():
    string: str = 'Hello, World!'
    print(string)


def printNoNewline(*args):
    for arg in args:
        print(arg, end=" ")


def clearPycache(path: str):
    shutil.rmtree(os.path.join(path, "__pycache__"))


def installModules(*args):
    for module in args:
        command: str = "python -m pip install {}".format(module)
        if subprocess.run(command):
            return True
        raise error.installModulesFailedError()

def alphabet() -> List[str]:
    theAlphabet: List[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return theAlphabet

def alphabetCaps() -> List[str]:
    theAlphabetCaps: List[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return theAlphabetCaps

def alphabetStr() -> str:
    theAlphabet: str = 'abcdefghijklmnopqrstwxyz'
    return theAlphabet

def alphabetCapsStr() -> str:
    theAlphabetCaps: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return theAlphabetCaps

def nums() -> List[int]:
    nums: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    return nums

def syms() -> List[str]:
    symbols: List[str] = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','\\',':',';','"','\'','<',',','>','.','?','/']
    return symbols
