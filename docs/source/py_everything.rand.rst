*****************************
:mod:`py_everything.rand`
*****************************

.. module:: py_everything.htmlXml

**Source code:** `py_everything/rand.py <https://github.com/pybash1/py_everything/blob/master/py_everything/rand.py>`_

This module Random generators for many things such as a random hex code generator, random RGB color generator,
random float generator, and much more!

.. function:: randhex()

    Generates a random hex color code such as ``#2A34FD``

    :returns string: The hex color code as a string

.. function:: randRGB()

    Generates a random RGB color and returns that as a tuple in the format - ``(red, green, blue)``

    :returns tuple: The RGB color as a tuple

.. function:: randletter()

    Generates a random alphabet and returns that as a string.

    :returns string: The random alphabet

.. function:: randint(start, end)

    Generates a random integer from among a given range and returns that

    :param int start: Start value of range
    :param int end: End value of range
    :returns int: The random integer

.. function:: randfloat(start, end)

    Generates a random float between given range
    
    :param float start: Start value of range
    :param float end: End value of range
    :returns float: The random float

.. function:: randbool()

    Generates a random boolean, either ``True`` or ``False``

    :returns bool: The random boolean

.. function:: randboolList(len)

    Generates a list of random boolean values
    
    :param int len: Length of list
    :returns list: The list of randomly generated boolean values

.. function:: randstring(string)

    Returns a random letter from a given string.
    
    :param str string: The string to choose random letter from
    :returns str: The random letter chosen from the string
