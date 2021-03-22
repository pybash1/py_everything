************************
py_everything.date_utils
************************

Import -
--------

How to import the module?

.. code:: python

   >>> import py_everything.date_utils as pyeDate

Get Current Date
----------------

Function Name - getDate()

No. of Parameters - 0

Parameters - None

Usage -
^^^^^^^

.. code:: python

   >>> pyeDate.getDate()
   2021-03-17

This function prints the current date.

Get Current Date and Time
-------------------------

Function Name - getDateTime()

No. of Parameters - 0

Parameters - None

Usage -
^^^^^^^

.. code:: python

   >>> pyeDate.getDateTime()
   2021-03-07 18:08:19.018239

This function prints the current date and time.

Get Current Time
----------------

Function Name - getTime()

No. of Parameters - 0

Parameters - None

Usage -
^^^^^^^

.. code:: python

   >>> pyeDate.getTime()
   18:09:13

This function prints the current time.

Get Date and Time in Custom Format
----------------------------------

Function Name - getCustomFormat(format)

No. of Parameters - 1

Parameters - format

Usage -
^^^^^^^

.. code:: python

   >>> pyeDate.getCustomFormat('%H:%M:%S')
   18:09:13

This function prints the current date or time in ``format``.

.. toctree::
   :caption: Basic:

.. toctree::
   :caption: Functions:

.. toctree::
   :caption: setupPyGen:

.. toctree::
   :caption: About the Project:
