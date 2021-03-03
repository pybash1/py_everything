import os
import subprocess
import shutil
from py_everything_exceptions import pycacheNotFoundError, installModulesFailedError


def hello_world():
    string = 'Hello, World!'
    return string


def print_no_newline(*args):
    for arg in args:
        print(arg, end=" ")


def clearPycache(path):
    if not shutil.rmtree(os.path.join(path, "__pycache__")):
        raise pycacheNotFoundError(
            "The '__pycache__' folder was not found in the given directory. Check if it exists and try again!")


def install_modules(*args):
    for module in args:
        command = f"python -m pip install {module}"
        if subprocess.run(command):
            return True
        else:
            raise installModulesFailedError

def docs():
    docs_string = '''This is the basic documentation for py_everything. For a more detailed and better documentation, please visit \'https://github.com/play4Tutorials/py_everything/tree/master/docs\'
There are total 9 files to import from. Each consisting of functions ranging from 5 to 20 and classes ranging from 1 to 3
Different files can be imported in this manner'''
