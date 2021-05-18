********************
py_everything.fileIO
********************

..currentmodule:: py_everything.fileIO

This module deals with files and their input/output operations. With a wide range of functions.

.. method:: readFile(fileName)

   This method reads data from ``fileName``.

   :param str fileName: Full path to the file to be read.
   :returns str: Data of the file.

.. method:: writeFile(fileName, writeData)

   This method writes new data - ``writeData`` on to ``fileName``

   :param str fileName: Full path to the file to writen to.
   :param str writeData: Data to be written on to the file.
   :returns bool: True if data was successfully written to file.

   .. note::
      This method deletes any previous data on the file. Before writing to it.

.. method:: clearFile(fileName)

   This method removes all data from ``fileName``.

   :param str fileName: Full path to the file to be cleared.
   :returns bool: True if file is cleared successfully.

.. method:: mkDir(dirName, path)

   Creates a new directory named ``dirName`` inside ``path``.

   :param str dirName: Name of the directory to be created.
   :param str path: Full path where directory is to be created.
   :returns bool: True if directory is created successfully.

.. method:: mkFile(fileName, path)

   Creates a new file named ``fileName`` inside ``path``.

   :param str fileName: Name of the file to be created.
   :param str path: Full path where file is to be created.
   :returns bool: True if file is created successfully.

.. method:: delDir(path, dirName)

   Deletes an existing directory named ``dirName`` from ``path``.

   :param str dirName: Name of the directory to be deleted.
   :param str path: Full path where directory is located.
   :returns bool: True if directory is deleted successfully.
   .. note::

      This function is for empty directories only, for directories containing files or subfolders, see the next method.

.. method:: delDirRec(path, dirName)

   Deletes an existing directory named ``dirName`` from ``path`` recursively.

   :param str dirName: Name of the directory to be deleted.
   :param str path: Full path where directory is located.
   :returns bool: True if directory is deleted successfully.

.. method:: delFile(path, fileName)

   Deletes an existing file named ``fileName`` from ``path``.

   :param str dirName: Name of the file to be deleted.
   :param str path: Full path where file is located.
   :returns bool: True if file is deleted successfully.
