import os, subprocess, time, random, shutil
from py_utils_exceptions import pycacheNotFoundError, installModulesFailedError

def hello_world():
    string = 'Hello, World!'
    return string

def print_no_newline(*args):
    for arg in args:
        print(arg, end=" ")

def clearPycache(path):
    if not shutil.rmtree(os.path.join(path, "__pycache__")):
        raise pycacheNotFoundError("The '__pycache__' folder was not found in the given directory. Check if it exists and try again!")

def install_modules(*args):
    for module in args:
        command = f"python -m pip install {module}"
        if subprocess.run(command):
            return True
        else:
            raise installModulesFailedError
