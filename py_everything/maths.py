from typing import Union, List, Dict
from py_expression_eval import Parser  # type: ignore
import math
from . import error


def add(num1: Union[int, float], num2: Union[int, float], *args) -> Union[int, float]:
    """Adds given numbers"""
    sum: Union[int, float] = num1 + num2
    for num in args:
        sum += num

    return sum


def subtract(num1: Union[int, float], num2: Union[int, float], *args) -> Union[int, float]:
    """Subtracts given numbers"""
    sub: Union[int, float] = num1 - num2
    for num in args:
        sub -= num
    return sub


def multiply(num1: Union[int, float], *args) -> Union[int, float]:
    """Multiplies given numbers"""
    product: Union[int, float] = num1
    for num in args:
        product = product * num
    return product


def divide(num1: Union[int, float], num2: Union[int, float], type: str) -> Union[int, float]:
    """Divides given numbers"""
    if type.lower() == 'int':
        int_quotient: Union[int, float] = num1 / num2
        return int_quotient
    if type.lower() == 'float':
        float_quotient: Union[int, float] = num1 // num2
        return float_quotient
    raise error.UnknownDivisionTypeError(type)


def floatDiv(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """Divides given numbers"""
    quotient: Union[int, float] = num1 / num2
    return quotient


def intDiv(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """Divides given numbers and returns rounded off integer as result"""
    quotient: Union[int, float] = num1 // num2
    return quotient


def expo(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """Raises given number to given power and returns result"""
    expo: Union[int, float] = num1 ** num2
    return expo


def mod(num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
    """Returns remainder of a division"""
    remain: Union[int, float] = num1 % num2
    return remain


def evalExp(exp: str, vars_: Dict[str, int] = {}):
    """Evaluates given mathematical expression"""
    parser = Parser()
    solution: Union[int, float] = parser.parse(exp).evaluate(vars_)
    return solution


def avg(listOfNos: Union[List[int], List[float]]) -> float:
    """Return average of given numbers"""
    avg: float = 0.0
    for num in listOfNos:
        avg += num

    avg = avg / len(listOfNos)
    return avg


def factorial(num: int) -> int:
    """Returns factorial of a number"""
    factorial: int = 1
    for i in range(1, num):
        factorial = factorial * i

    return factorial


def ceil(num: int) -> int:
    """Returns the number rounded up"""
    ceil: int = math.ceil(num)
    return ceil


def floor(num: int) -> int:
    """Returns the number rounded down"""
    floor: int = math.floor(num)
    return floor
