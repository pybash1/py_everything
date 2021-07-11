****************************
:mod:`py_everything.search`
****************************

.. module:: py_everything.search

**Source code:** `py_everything/search.py <https://github.com/pybash1/py_everything/blob/master/py_everything/search.py>`_

This module deals with search operations, like files, lists, etc.

.. function:: searchFiles(keyword, path)

   Searches ``path`` for files matching with ``keyword``.

   :param str keyword: Word to match files with
   :param str path: Full path to directory to search in
   :returns list: List of matches

.. function:: searchDirs(keyword, path)

   Searches ``path`` for directories matching with ``keyword``.

   :param str keyword: Word to match directories with
   :param str path: Full path to directory to search in
   :returns list: List of matches

.. function:: searchExts(keyword, path)

   Searches ``path`` for file extensions matching with ``keyword``.

   :param str keyword: Extension to match file extensions with
   :param str path: Full path to directory to search in
   :returns list: List of matches

.. function:: searchList(listOfTerms, query, filter='in)

   Searches ``listOfTerms`` for terms matching with ``query``.

   :param str listOfTerms: List to search in
   :param str query: Word to verify matches with
   :param filter: Specify way if searching. Choices - 'in', 'start', 'end', 'exact'.
   :returns list: List of matches

   .. note:: 

      ``filter`` is set to 'in' by default. 'in' - Checks if ``query`` is
      in term. 'start' - Checks if term starts with ``query``.
      'end' - Checks if term ends with ``query``. 'exact' - Checks if
      term == ``query``.

