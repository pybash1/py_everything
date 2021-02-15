import os
import subprocess

def add(num1, num2, *args):
    sum = num1 + num2
    for num in args:
        sum += num

    return sum

def subtract(num1, num2, *args):
    sub = num1 - num2
    for num in args:
        sub = sub - num
    return sub

def multiply(num1, *args):
    product = num1
    for num in args:
        product = product * num

def divide(num1, num2, type):
    if type.lower() == 'int':
        int_quotient = num1 / num2
        return int_quotient
    else:
        float_quotient = num1 // num2
        return float_quotient

def float_div(num1, num2):
    quotient = num1 // num2
    return quotient

def int_div(num1, num2):
    quotient = num1 / num2
    return quotient

def expo(num1, num2):
    expo = num1 ^ num2

def mod(num1, num2):
    remain = num1 % num2
    return remain

def install_modules(*args):
    for module in args:
        command = f"pip install {module}"
        subprocess.run(command)

def search_files(keyword, path):
    files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if keyword in file:
                files.append(root + '\\' + str(file))

    return files

def search_dirs(keyword, path):
    folders = []
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            if keyword in dir:
                folders.append(root + '\\' + str(dir))
    return folders

def search_exts(ext, path):
    files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith(ext):
                files.append(root + '\\' + str(file))

