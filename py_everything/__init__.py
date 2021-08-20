import os
import subprocess
import shutil
from . import error
from typing import List

# Variables for the package
__author__: str = "PyBash"
__version__: str = "v2.0.0"


def helloWorld():
    """Prints hello world"""
    string: str = 'Hello, World!'
    print(string)


def printNoNewline(*args):
    """Prints given arguments without newline"""
    for arg in args:
        print(arg, end=" ")


def clearPycache(path: str):
    """Deletes __pycache__ directory from given path"""
    shutil.rmtree(os.path.join(path, "__pycache__"))


def installModules(*args):
    """Installs modules passed into args"""
    for module in args:
        command: str = "python -m pip install {}".format(module)
        if subprocess.run(command):
            return True
        raise error.installModulesFailedError()


def alphabet() -> List[str]:
    """Returns all alphabets as a list"""
    theAlphabet: List[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k',
                              'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    return theAlphabet


def alphabetCaps() -> List[str]:
    """Returns all capital alphabets as a list"""
    theAlphabetCaps: List[str] = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                                  'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    return theAlphabetCaps


def alphabetStr() -> str:
    """Returns all alphabets as a string"""
    theAlphabet: str = 'abcdefghijklmnopqrstwxyz'
    return theAlphabet


def alphabetCapsStr() -> str:
    """Returns all capital alphabets as a string"""
    theAlphabetCaps: str = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return theAlphabetCaps


def nums() -> List[int]:
    """Returns all digits as a list"""
    nums: List[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    return nums


def syms() -> List[str]:
    """Returns all speacial characters as a list"""
    symbols: List[str] = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*',
                          '(', ')', '_', '-', '+', '=', '{', '[', '}', '}', '|', '\\', ':', ';', '"', '\'', '<', ',', '>', '.', '?', '/']
    return symbols


def symsStr() -> str:
    """Returns all speacial characters as a string"""
    symbols: str = '`~!@#$%^&*()_-+={[]}|\\:;"\'<,>.?/'
    return symbols
