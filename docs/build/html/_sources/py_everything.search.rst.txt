.. sectionauthor:: Play 4 Tutorials <play.4.tutotials@gmail.com>

********************
py_everything.search
********************

Import -
--------

How to import the module?

.. code:: python

   >>> import py_everything.search as pyeSearch

Search Files
------------

Function Name - search_files(keyword, path)

No. of Parameters - 2

Parameters - keyword, path

Usage -
^^^^^^^

.. code:: python

   >>> pyeSearch.search_files("mykeyword", "D:")
   ['D:\mykeyword.txt', 'D:\file-with-mykeyword.pdf', 'D:\myfolder\pymykeyword.py']

This function searches for files with ``keyword`` in them in ``path``.
And returns a list containing the full path of those files.

Search Folders
--------------

Function Name - search_dirs(keyword, path)

No. of Parameters - 2

Parameters - keyword, path

Usage -
^^^^^^^

.. code:: python

   >>> pyeSearch.search_dirs("myfolder", "D:")
   ['D:\folder\myfolder', 'D:\myfolder-py']

This function searches for folders or directories with ``keyword`` in
them in ``path``. And returns a list containing the full path of those
folders or directories.

Search by Extension
-------------------

Function Name - search_exts(ext, path)

No. of Parameters - 2

Parameters - ext, path

Usage -
^^^^^^^

.. code:: python

   >>> pyeSearch.search_exts("txt", "D:")
   ['D:\folder\file.txt', 'D:\py.txt']

This function searches for files with the extension ``ext`` in ``path``.
And returns a list containing the full path of those files.

Search in Lists
---------------

Function Name - search_list(listOfTerms, query, filter='in')

No. of Parameters - 3

Parameters - listOfTerms, query, filter

Usage -
^^^^^^^

.. code:: python

   >>> mylist = ["python", "pipypi", "py", "endpy", "other", "file", "everything"]
   >>> pyeSearch.search_list(mylist, "py", filter="in")
   ['python', 'pipypi', 'py', 'endpy']
   >>> pyeSearch.search_list(mylist, "py", filter="start")
   ['python', 'py']
   >>> pyeSearch.search_list(mylist, "py", filter="end")
   ['endpy']
   >>> pyeSearch.search_list(mylist, "py", filter="exact")
   ['py']

This function searches for items with ``query`` in them in
``listOfItem``. And returns a list containing the items. ``filter`` can
have 4 values, i.e., 'in', 'start', 'end', 'exact'. 'in' returns items
which have ``query`` in them. 'start' returns items which start with
``query``. 'end' returns items which end with ``query``. 'exact' returns
items which are exactly the ``query``.

.. toctree::
   :caption: Basic:

.. toctree::
   :caption: Functions:

.. toctree::
   :caption: About the Project:
