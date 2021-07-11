*************************
:mod:`py_everything.path`
*************************

.. module:: py_everything.path

**Source code:** `py_everything/path.py <https://github.com/pybash1/py_everything/blob/master/py_everything/path.py>`_

This module deals with paths, local or web.

.. versionadded:: 2.1.0

.. class:: Path(path)

    This class contains all functions related to Path.

    .. note::
    The REGEX's used to check the path can also be used, you need to import them.

    :param path: String containing full path(web or local)
    :type path: str

    :raises error.UnknownPathTypeError: Raised if path type can't be determined.

    .. function:: getType()

        Returns type of file as ``str``('local' or 'web')

        :returns str: Type of file('local' or 'web')

    .. function:: getRawPath()

        Returns raw input path as-is without any modifications.

        :returns str: Raw Input Path as-is
        :raises error.InvalidOperationPerformedError: This is raised if the path type is web

    .. function:: getRealPath()

        Returns real path based on system type and os.

        :returns str: Real Path based on system type and operating system
        :raises error.InvalidOperationPerformedError: This is raised if the path type is web

    .. function:: isFile()

        Returns boolean depending on if the path is to a file or a folder.

        :returns bool: True if the path is to a file
        :raises error.InvalidOperationPerformedError: This is raised if the path type is web

    .. function:: isDir()

        Returns boolean depending on if the path is to a file or a folder.

        :returns bool: True if the path is to a folder/directory
        :raises error.InvalidOperationPerformedError: This is raised if the path type is web

    .. function:: getRelativePath()

        Returns path relative to ``os.curdir``

        :returns str: Path relative to ``os.curdir``
        :raises error.InvalidOperationPerformedError: This is raised if the path type is web

    .. function:: getLastAccessTime()

        Returns last accessed time for file/folder.

        :raises error.InvalidOperationPerformedError: This is raised if the path type is web
    
    .. function:: getLastModifiedTime()

        Returns last modified time for file/folder.

        :raises error.InvalidOperationPerformedError: This is raised if the path type is web
    
    .. function:: openInBrowser()

        Opens URL in default browser.

        :raises error.InvalidOperationPerformedError: This is raised if the path type is local
    
    .. function:: getRequest()

        Returns Requests Response Object.

        :returns: Response object of get request to URL
        :raises error.InvalidOperationPerformedError: This is raised if the path type is local
    
    .. function:: getRequestStatusCode()

        Returns status code for get request to URL.

        :returns int: Status code
        :raises error.InvalidOperationPerformedError: This is raised if the path type is local
