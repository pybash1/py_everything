from typing import Union, List
import math,  ast
from . import error

def add(num1: Union[int, float], num2: Union[int, float], *args) -> Union[int, float]:
    sum: Union[int, float] = num1 + num2
    for num in args:
        sum += num

    return sum


def subtract(num1: Union[int, float], num2: Union[int, float], *args) -> Union[int, float]:
    sub: Union[int, float] = num1 - num2
    for num in args:
        sub -= num
    return sub


def multiply(num1: Union[int, float], *args) -> Union[int, float]:
    product: Union[int, float] = num1
    for num in args:
        product = product * num
    return product


def divide(num1: Union[int, float], num2: Union[int, float], type: str) -> Union[int, float]:
    if type.lower() == 'int':
        int_quotient: Union[int, float] = num1 / num2
        return int_quotient
    if type.lower() == 'float':
        float_quotient: Union[int, float] = num1 // num2
        return float_quotient
    raise error.UnknownDivisionTypeError(type)


def floatDiv(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    quotient: Union[int, float] = num1 / num2
    return quotient


def intDiv(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    quotient: Union[int, float] = num1 // num2
    return quotient


def expo(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    expo: Union[int, float] = num1 ** num2
    return expo


def mod(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    remain: Union[int, float] = num1 % num2
    return remain


def evalExp(exp):
    solution: Union[int, float] = ast.literal_eval(exp)
    return solution

def avg(listOfNos: Union[List[int], List[float]]) -> float:
    avg: float = 0.0
    for num in listOfNos:
        avg += num

    avg = avg / len(listOfNos)
    return avg

def factorial(num: int) -> int:
    factorial: int = 1
    for i in range(1, num):
        factorial = factorial * i
        
    return factorial

def ceil(num: int) -> int:
    ceil: int = math.ceil(num)
    return ceil
    
def floor(num: int) -> int:
    floor: int = math.floor(num)
    return floor
