import os
import subprocess
import shutil

def hello_world():
    string = 'Hello, World!'
    print(string)


def print_no_newline(*args):
    for arg in args:
        print(arg, end=" ")


def clearPycache(path):
    if not shutil.rmtree(os.path.join(path, "__pycache__")):
        return False
    else:
        return True


def install_modules(*args):
    for module in args:
        command = "python -m pip install {}".format(module)
        if subprocess.run(command):
            return True
        else:
            return False
