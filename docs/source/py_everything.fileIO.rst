****************************
:mod:`py_everything.fileIO`
****************************

.. module:: py_everything.fileIO

**Source code:** `py_everything/fileIO.py <https://github.com/pybash1/py_everything/blob/master/py_everything/fileIO.py>`_

This module deals with files and their input/output operations. With a wide range of functions.

.. function:: readFile(fileName)

   This method reads data from ``fileName``.

   :param str fileName: Full path to the file to be read.
   :returns str: Data of the file.

.. function:: writeFile(fileName, writeData)

   This method writes new data - ``writeData`` on to ``fileName``

   :param str fileName: Full path to the file to writen to.
   :param str writeData: Data to be written on to the file.
   :returns bool: True if data was successfully written to file.

   .. versionchanged:: 2.0.0
      Raises :exc:`TypeError` if ``writeData`` type is not ``str``

   .. note::
      This method deletes any previous data on the file. Before writing to it.

.. function:: clearFile(fileName)

   This method removes all data from ``fileName``.

   :param str fileName: Full path to the file to be cleared.
   :returns bool: True if file is cleared successfully.

.. function:: mkDir(dirName, path)

   Creates a new directory named ``dirName`` inside ``path``.

   :param str dirName: Name of the directory to be created.
   :param str path: Full path where directory is to be created.
   :returns bool: True if directory is created successfully.

.. function:: mkFile(fileName, path)

   Creates a new file named ``fileName`` inside ``path``.

   :param str fileName: Name of the file to be created.
   :param str path: Full path where file is to be created.
   :returns bool: True if file is created successfully.

.. function:: delDir(path, dirName)

   Deletes an existing directory named ``dirName`` from ``path``.

   :param str dirName: Name of the directory to be deleted.
   :param str path: Full path where directory is located.
   :returns bool: True if directory is deleted successfully.
   .. note::

      This function is for empty directories only, for directories containing files or subfolders, see the next method.

.. function:: delDirRec(path, dirName)

   Deletes an existing directory named ``dirName`` from ``path`` recursively.

   :param str dirName: Name of the directory to be deleted.
   :param str path: Full path where directory is located.
   :returns bool: True if directory is deleted successfully.

.. function:: delFile(path, fileName)

   Deletes an existing file named ``fileName`` from ``path``.

   :param str dirName: Name of the file to be deleted.
   :param str path: Full path where file is located.
   :returns bool: True if file is deleted successfully.
