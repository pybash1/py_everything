
def add(num1, num2, *args):
    sum = num1 + num2
    for num in args:
        sum += num

    return sum


def subtract(num1, num2, *args):
    sub = num1 - num2
    for num in args:
        sub -= num
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
    quotient = num1 / num2
    return quotient


def int_div(num1, num2):
    quotient = num1 // num2
    return quotient


def expo(num1, num2):
    expo = num1 ^ num2
    return expo


def mod(num1, num2):
    remain = num1 % num2
    return remain


def eval_exp(exp):
    solution = eval(exp)
    return solution

def avg(listOfNos):
    avg = 0
    for num in listOfNos:
        avg += num

    avg = avg / len(listOfNos)
    return avg

class MathsBase:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def add(self, num1, num2, *args):
        sum = num1 + num2
        for num in args:
            sum += num

        return sum

    def subtract(self, num1, num2, *args):
        sub = num1 - num2
        for num in args:
            sub = sub - num
        return sub

    def multiply(self, num1, *args):
        product = num1
        for num in args:
            product = product * num

    def divide(self, num1, num2):
        quotient = num1 / num2
        return quotient


class MathsAdvanced:
    def __init__(self, num1=0, num2=0):
        self.num1 = num1
        self.num2 = num2

    def add(self, num1, num2, *args):
        sum = num1 + num2
        for num in args:
            sum += num

        return sum

    def subtract(self, num1, num2, *args):
        sub = num1 - num2
        for num in args:
            sub = sub - num
        return sub

    def multiply(self, num1, *args):
        product = num1
        for num in args:
            product = product * num

    def divide(self, num1, num2, type):
        if type.lower() == 'int':
            int_quotient = num1 / num2
            return int_quotient
        else:
            float_quotient = num1 // num2
            return float_quotient

    def float_div(self, num1, num2):
        quotient = num1 / num2
        return quotient

    def int_div(self, num1, num2):
        quotient = num1 // num2
        return quotient

    def expo(self, num1, num2):
        expo = num1 ^ num2
        return expo

    def mod(self, num1, num2):
        remain = num1 % num2
        return remain

    def eval_exp(self, exp):
        solution = eval(exp)
        return solution

    def avg(self, listOfNos):
        avg = 0
        for num in listOfNos:
            avg += num

        avg = avg / len(listOfNos)
        return avg
