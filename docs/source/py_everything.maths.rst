**************************
:mod:`py_everything.maths`
**************************

.. module:: py_everything.maths

**Source code:** `py_everything/maths.py <https://github.com/pybash1/py_everything/blob/master/py_everything/maths.py>`_

This module deals with mathematical functions and operations.

.. function:: add(num1, num2, *args)

   Function for adding 2 or more numbers.

   :param Union num1: First Number.
   :param Union num2: Second Number.
   :param *args: Rest numbers.
   :returns Union: Result

.. function:: subtract(num1, num2, *args)

   Function for subtracting 2 or more numbers.

   :param Union num1: First Number.
   :param Union num2: Second Number.  
   :param *args: Rest numbers.  
   :returns Union: Result

.. function:: multiply(num1, num2, *args)

   Function for multipling 2 or more numbers.

   :param Union num1: First Number.
   :param Union num2: Second Number.  
   :param *args: Rest numbers.  
   :returns Union: Result

.. function:: divide(num1, num2, type)

   Function for dividing 2 numbers.

   :param Union num1: First Number.
   :param Union num2: Second Number.  
   :param str type: Integer division or float division.  
   :returns Union: Result
   :raises error.UnknownDivisionTypeError: Raised if division type can't be determined.

.. function:: floatDiv(num1, num2)

   :param Union num1: First Number.
   :param Union num2: Second Number.
   :returns Union: Result

.. function:: intDiv(num1, num2)

   :param Union num1: First Number.
   :param Union num2: Second Number.
   :returns Union: Result

.. function:: expo(num1, num2)

   :param Union num1: First Number.
   :param Union num2: Second Number.
   :returns Union: Result

.. function:: mod(num1, num2)

   :param Union num1: First Number.
   :param Union num2: Second Number.
   :returns Union: Result

.. function:: evalExp(exp)

   :param Union exp: Mathematical Expression

.. function:: avg(listOfNos)

   :param Union listOfNos: List Of Nos. for average.
   :returns float: Average of nos.

.. function:: factorial(num)

   :param Union num: Number for Factorial.
   :returns int: Result of factorial

.. function:: ceil(num)

   :param Union num: Number for rounding up.
   :returns int: Result

.. function:: floor(num)

   :param Union num: Number for rounding down.
   :returns int: Result
