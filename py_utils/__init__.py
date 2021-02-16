import os, subprocess, time, random, shutil
from py_utils_exceptions import pycacheNotFoundError

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
        subprocess.run(command)

def help_me():
    base = 'This command gives you a list of all available functions and classes.'
    funcList = ['hello_world()', 'print_no_newline()', 'clearPycache()', 'install_modules()', 'help_me()', 'date_utils.*()', 'date_utils.get_date()', 'date_utils.get_date_time()', 'date_utils.get_time()', 'date_utils.get_custom_format()', 'fileIO.*()', 'fileIO.read_file()', 'fileIO.write_file()', 'maths.*()', 'maths.add()',  'maths.subtract()',  'maths.multiply()',  'maths.divide()',  'maths.int_div()',  'maths.float_div()',   'maths.mod()', 'maths.eval_exp()', 'requestsLib.*()', 'search.*()']
    print(base)
    time.sleep(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
    for item in funcList:
        return item
