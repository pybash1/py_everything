*************
py_everything
*************

.. currentmodule:: py_everything

This module contains some basic functions. This is the base module of the library.

.. method:: helloWorld()

   Super Simple and Basic function that prints "Hello, World!"

.. method:: printNoNewline(*args)

   Prints text without newlines. Very basic function.

   :param *args: The text you want to print without newlines

   .. note::

      You cannot customize what is printed instead of the newline.

.. method:: clearPycache(path)

   Deletes *__pycache__* folder from `path`.

   :param str path: Full path to the folder which contains *__pycache__*
   :returns bool: True if *__pycache__* is deleted successfully.
   :raises error.pycacheNotFoundError: This exception is raised if ``path`` does not contain
                           ``__pycache__``.

.. method:: installModules(*args)

   Install modules using ``pip``, while execution.

   :param *args: Modules you want to install.
   :returns bool: True if all modules were installed successfully.
   :raises error.installModulesFailedError: This exception is raised if all modules could not be
                                             installed successfully. Occurs if package doesn't exist.

.. method:: alphabet()

   Get a list of all alphabets in lowercase.

   :returns list: List containing all alphabets in lowercase in alphabetical order.

.. method:: alphabetCaps()

   Get a list of all alphabets in uppercase.

   :returns list: List containing all alphabets in uppercase in alphabetical order.

.. method:: alphabetStr()

   Get a string of all alphabets in lowercase.

   :returns str: String containing all alphabets in lowercase in alphabetical order.

.. method:: alphabetCapsStr()

   Get a string of all alphabets in uppercase.

   :returns str: String containing all alphabets in uppercase in alphabetical order.

.. method:: nums()

   Get a list of all numbers(0-9).

   :returns list: List containing all numbers(0-9) in ascending order.

.. method:: syms()

   Get a list of all symbols.

   :returns list: List containing all symbols.
