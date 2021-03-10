********************
py_everything.fileIO
********************

Import -
--------

How to import the module?

.. code:: python

   >>> import py_everything.fileIO as pyeFiles

Read Data from a File
---------------------

Function Name - read_file(filename)

No. of Parameters - 1

Parameter - filename

Usage -
^^^^^^^

.. code:: python

   >>> pyeFiles.read_file('path/to/file')
   Data of the file is returned.

This function reads the data of ``filename`` and returns it.

Write Data to a File
--------------------

Function Name - write_file(filename, writeData='')

No. of Parameters - 2

Parameter - filename, writeData

Usage -
^^^^^^^

.. code:: python

   >>> pyeFiles.write_file('path/to/file', writeData="Data to be written to the file.")
   True

This function reads the file given in ``filename``, then clears all its
content and then writes ``writeData`` to the file. If these steps are
successful, it returns True.

Clear or Erase Contents of a File
---------------------------------

Function Name - write_file(filename)

No. of Parameters - 1

Parameter - filename

Usage -
^^^^^^^

.. code:: python

   >>> pyeFiles.clear_file('path/to/file')
   True

This function reads the file given in ``filename``, then clears all its
contents. If the steps are successful, it returns True.

Make a New :term:`directory` or Folder
------------------------------

Function Name - mk_dir(dir_name, path)

No. of Parameters - 2

Parameter - dir_name, path

Usage -
^^^^^^^

.. code:: python

   >>> pyeFiles.mk_dir('folderName', 'path/to/folder')
   True

This function makes a new :term:`directory` named ``dir_name`` in ``path``. If
steps are successful, returns True.

Make a New File
---------------

Function Name - mk_file(file_name, path)

No. of Parameters - 2

Parameter - file_name, path

Usage -
^^^^^^^

.. code:: python

   >>> pyeFiles.mk_file('fileName.txt', 'path/to/file/location')
   True

This function makes a new file named ``file_name`` in ``path``. If steps
are successful, returns True.

Delete an Empty :term:`directory`
-------------------------

Function Name - del_dir(path, dir_name)

No. of Parameters - 2

Parameter - path, dir_name

Usage -
^^^^^^^

.. code:: python

   >>> pyeFiles.del_dir('folderName', 'path/to/folder')
   True

This function deletes an existing empty :term:`directory` named ``dir_name``
that is in ``path``. If steps are successful, returns True. Raises error
if :term:`directory` is not empty or does not exist.

Delete a :term:`directory` with Items(Recursive Deletion)
-------------------------------------------------

Function Name - del_dir_rec(path, dir_name)

No. of Parameters - 2

Parameter - path, dir_name

Usage -
^^^^^^^

.. code:: python

   >>> pyeFiles.del_dir_rec('folderName', 'path/to/folder')
   True

This function deletes an existing :term:`directory` named ``dir_name`` that is
in ``path``. It deletes it regardless, it is empty or has items. If
steps are successful, returns True. Raises error if direectory does not
exist.

Delete a File
-------------

Function Name - del_file(path, file_name)

No. of Parameters - 2

Parameter - path, file_name

Usage -
^^^^^^^

.. code:: python

   >>> pyeFiles.del_file('fileName.txt', 'path/to/file/location')
   True

This function deletes an existing file named ``file_name`` that is in
``path``. If steps are successful, returns True. Raises error if file
does not exist.

.. toctree::
   :caption: Basic:

.. toctree::
   :caption: Functions:

.. toctree::
   :caption: About the Project:
