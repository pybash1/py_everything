************************
py_everything.dateUtils
************************

.. currentmodule:: py_everything.dateUtils

This module deals date and time. Like, fetching current date, time, etc.

.. method:: getDate()

   This method fetches the date the program is being executed on.

   :returns: The date program is being executed on.

.. method:: getDateTime()

   This method fetches the date and time the program is being executed on.

   :returns: The date and time program is being executed on.

   .. note ::

      This method returns a float for seconds of the time, like, 12 seconds would be 12.45365. It is very precise.

.. method:: getTime()

   This method fetches the time the program is being executed on.

   :returns: The time program is being executed on.

.. method:: getCustomFormat(format)

   This method fetches the date and/or time in a custom format.

   :param str format: The format in which the date and/or time should be returned.
   :returns: The date and/or current time.

   .. note:: 

      strftime format is used in ``format``. To know more about it see `this <https://docs.python.org/3/library/datetime.html#datetime.time.strftime>`_ and `this <https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior>`_.

