import os
import subprocess
import shutil

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
        return False


def installModules(*args):
    for module in args:
        command = "python -m pip install {}".format(module)
        if subprocess.run(command):
            return True
        else:
            return False
