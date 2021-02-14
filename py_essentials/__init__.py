def add(num1, *args):
    sum = num1
    for num in args:
        sum += num

    return sum

def subtract(num1, num2):
    sub = num1 - num2
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

def expo(num1, num2):
    expo = num1 ^ num2
