.. sectionauthor:: Play 4 Tutorials <play.4.tutotials@gmail.com>

*************
py_everything
*************

Import -
--------

How to import the module?

.. code:: python

   >>> import py_everything as pye

Your First Program using this package
-------------------------------------

What's the best way to write your first program than "Hello, World!"

Function name - hello_world()

No. of Parameters - 0

Parameters - No parameters

Usage -
^^^^^^^

.. code:: python

   >>> pye.hello_world()
   Hello, World!

So, we wrote our first program. Let's move on.

Clear pycache
-------------

Function name - clearPycache(path)

No. of Parameters - 1

Parameters - path

Usage -
^^^^^^^

.. code:: python

   >>> pye.clearPycache(path\to\pycache\folder)
   True

Provide the pth to the folder where the "**\__pycache_\_**" is located.
For example - C:\Programming\Projects\Python

Note - Do not provide **\__pycache_\_** in the path. That does not clear
it. For example - C:\Programming\Projects\Python\__pycache__. This would
return False.

Print without newline
---------------------

Function name - print_no_newline(\*args)

No. of Parameters - infinte

Parameters - \*args

Usage -
^^^^^^^

.. code:: python

   >>> pye.print_no_newline("hello", "world", "this is printed without newline", ".")
   hello world this is printed without newline .

Pass in the words you want to get printed without newline and That will
be printed.

Install modules with pip
------------------------

Function name - install_modules(\*args)

No. of Parameters - infinte

Parameters - \*args

Usage -
^^^^^^^

.. code:: python

   >>> pye.install_modules("py_everything", "requests")
   True

This function install the given modules using ``pip``. If the command is
successful it returns True else False.

.. toctree::
   :caption: Basic:
.. toctree::
   :caption: Functions:

.. toctree::
   :caption: About the Project:
