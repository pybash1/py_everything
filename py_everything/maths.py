from typing import Union
import math

def add(num1: Union[int, float], num2: Union[int, float], *args) -> Union[int, float]:
    sum = num1 + num2
    for num in args:
        sum += num

    return sum


def subtract(num1: Union[int, float], num2: Union[int, float], *args) -> Union[int, float]:
    sub = num1 - num2
    for num in args:
        sub -= num
    return sub


def multiply(num1: Union[int, float], *args) -> Union[int, float]:
    product = num1
    for num in args:
        product = product * num
    return product


def divide(num1: Union[int, float], num2: Union[int, float], type: str) -> Union[int, float]:
    if type.lower() == 'int':
        int_quotient = num1 / num2
        return int_quotient
    else:
        float_quotient = num1 // num2
        return float_quotient


def floatDiv(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    quotient = num1 / num2
    return quotient


def intDiv(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    quotient = num1 // num2
    return quotient


def expo(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    expo = num1 ** num2
    return expo


def mod(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    remain = num1 % num2
    return remain


def evalExp(exp):
    solution = eval(exp)
    return solution

def avg(listOfNos) -> float:
    avg = 0
    for num in listOfNos:
        avg += num

    avg = avg / len(listOfNos)
    return avg

def factorial(num: int) -> int:
    factorial = 1
    for i in range(1, num):
        factorial = factorial * i
        
    return factorial

def ceil(num: int) -> int:
    ceil = math.ceil(num)
    return ceil
    
def floor(num: int) -> int:
    floor = math.floor(num)
    return floor
