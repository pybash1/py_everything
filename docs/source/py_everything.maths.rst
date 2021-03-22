*******************
pyEverything.maths
*******************

Import -
--------

How to import the module?

.. code:: python

   >>> import pyEverything.maths as pyeMaths

Add
---

Function Name - add(num1, num2, \*args)

No. of Parameters - infinite

Parameters - num1, num2, \*args

Usage -

.. code:: python

   >>> pyeMaths.add(1, 4, 3, 7, 3, 10, 13, 24)
   65

Subtract
--------

Function Name - subtract(num1, num2, \*args)

No. of Parameters - infinite

Parameters - num1, num2, \*args

Usage -

.. code:: python

   >>> pyeMaths.subtract(16, 4, 3)
   9

Multiply
--------

Function Name - multiply(num1, \*args)

No. of Parameters - infinite

Parameters - num1, \*args

Usage -

.. code:: python

   >>> pyeMaths.multiply(2, 4, 3)
   24

Divide
------

Function Name - divide(num1, num2, type)

No. of Parameters - 3

Parameters - num1, num2, type

Usage -

.. code:: python

   >>> pyeMaths.divide(36, 3, 'float')
   12.0
   >>> pyeMaths.divide(36, 3, 'int')
   12

Float Division
--------------

Function Name - floatDiv(num1, num2)

No. of Parameters - 2

Parameters - num1, num2

Usage -

.. code:: python

   >>> pyeMaths.floatDiv(36, 3)
   12.0

Integer Division
----------------

Function Name - intDiv(num1, num2)

No. of Parameters - 2

Parameters - num1, num2

Usage -

.. code:: python

   >>> pyeMaths.intDiv(36, 3)
   12

Exponent
--------

Function Name - expo(num1, num2)

No. of Parameters - 2

Parameters - num1, num2

Usage -

.. code:: python

   >>> pyeMaths.expo(2, 4)
   16

Modulus
-------

Function Name - mod(num1, num2)

No. of Parameters - 2

Parameters - num1, num2

Usage -

.. code:: python

   >>> pyeMaths.mod(17, 2)
   1

Evaluate Any Mathematics Expression
-----------------------------------

Function Name - evalExp(exp)

No. of Parameters - 1

Parameters - exp

Usage -

.. code:: python

   >>> pyeMaths.expo('2 + 4 - 1 * 2')
   10

Average
-------

Function Name - avg(listOfNos)

No. of Parameters - 1

Parameters - listOfNos

Usage -

.. code:: python

   >>> pyeMaths.avg(['2', '3', '1', '5', '8', '4', '3'])
   3.7142857142857144

Note
----
These functions have not been explained seperately because they explain themselves.

.. toctree::
   :caption: Basic:

.. toctree::
   :caption: Functions:

.. toctree::
   :caption: setupPyGen:

.. toctree::
   :caption: About the Project:
