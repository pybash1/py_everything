*****************************
:mod:`py_everything.htmlXml`
*****************************

.. module:: py_everything.htmlXml

**Source code:** `py_everything/htmlXml.py <https://github.com/pybash1/py_everything/blob/master/py_everything/htmlXml.py>`_

This module deals with HTML/XML Files. This module will be extended in later releases.
With functions that fetch tags from document for you to a class allowing all methods in one!
This module doesn't check if the HTML/XML file is valid or not. It will return matches if a
certain tag is not closed. This module was added in version 2.0.0

.. class:: HTMLObject(fileName)

    This class access to all methods without having to give the fileName everytime.

    .. code:: python

        >>> from py_everything.html import HTMLObject
        >>> myHtml = HTMLObject('C:/index.html')
        >>> divs = myHtml.getElementsByTag('div')
        >>> divs
        ["<div id='app'>This is main app</div>", "<div>Other part of HTML</div>"]
        >>> title = myHtml.getElementByTag('title')
        >>> title
        ['<title>Demo Website</title>']
        >>> mainApp = myHtml.getElementById('app)
        >>> mainApp
        ["<div id='app'>This is main app</div>"]

    :param fileName: A string containing full path to HTML/XML file.
    :type fileName: str

    .. function:: getElementsByTag(tagName)

        Searches HTML/XML file for given ``tagName``.

        :param str tagName: The tag you want to search for.
        :returns list: A list containing all matches in str.

        .. note::

            The whole line is returned if a match is found. And the tag is not validated.

    .. function:: getElementsById(idName)

        Searches HTML/XML file for given tags with the id of ``idName``.

        :param str idName: The id you want to search for.
        :returns list: A list containing all matches in str.

        .. note::

            The whole line is returned if a match is found. And the tag is not validated.

    .. function:: getElementsByClass(className)

        Searches HTML/XML file for given tags with the class of ``className``.

        :param str className: The class you want to search for.
        :returns list: A list containing all matches in str.

        .. note::

            The whole line is returned if a match is found. And the tag is not validated.

    .. function:: getElementByTag(tagName)

        Searches HTML/XML file for given ``tagName``. And returns only the first match.

        :param str tagName: The tag you want to search for.
        :returns list: A list containing first match in str.

        .. note::

            The whole line is returned if a match is found. And the tag is not validated.

    .. function:: getElementById(idName)

        Searches HTML/XML file for given tags with the id of ``idName``. And returns only the first match.

        :param str idName: The id you want to search for.
        :returns list: A list containing first match in str.

        .. note::

            The whole line is returned if a match is found. And the tag is not validated.

    .. function:: getElementByClass(className)

        Searches HTML/XML file for given tags with the class of ``className``. And returns only the first match.

        :param str className: The class you want to search for.
        :returns list: A list containing first match in str.

        .. note::

            The whole line is returned if a match is found. And the tag is not validated.





.. function:: getElementsByTag(tagName, fileName)

    Searches HTML/XML file ``fileName`` for given ``tagName``.

    :param str tagName: The tag you want to search for.
    :param str fileName: A string containing full path to HTML/XML file.
    :returns list: A list containing all matches in str.

    .. note::

        The whole line is returned if a match is found. And the tag is not validated.

.. function:: getElementsById(idName, fileName)

    Searches HTML/XML file ``fileName`` for given tags with the id of ``idName``.

    :param str idName: The id you want to search for.
    :param str fileName: A string containing full path to HTML/XML file.
    :returns list: A list containing all matches in str.

    .. note::

        The whole line is returned if a match is found. And the tag is not validated.

.. function:: getElementsByClass(className, fileName)

    Searches HTML/XML file ``fileName`` for given tags with the class of ``className``.

    :param str className: The class you want to search for.
    :param str fileName: A string containing full path to HTML/XML file.
    :returns list: A list containing all matches in str.

    .. note::

        The whole line is returned if a match is found. And the tag is not validated.

.. function:: getElementByTag(tagName, fileName)

    Searches HTML/XML file ``fileName`` for given ``tagName``. And returns only the first match.

    :param str tagName: The tag you want to search for.
    :param str fileName: A string containing full path to HTML/XML file.
    :returns list: A list containing first match in str.

    .. note::

        The whole line is returned if a match is found. And the tag is not validated.

.. function:: getElementById(idName, fileName)

    Searches HTML/XML file ``fileName`` for given tags with the id of ``idName``. And returns only the first match.

    :param str idName: The id you want to search for.
    :param str fileName: A string containing full path to HTML/XML file.
    :returns list: A list containing first match in str.

    .. note::

        The whole line is returned if a match is found. And the tag is not validated.

.. function:: getElementByClass(className, fileName)

    Searches HTML/XML file ``fileName`` for given tags with the class of ``className``. And returns only the first match.

    :param str className: The class you want to search for.
    :param str fileName: A string containing full path to HTML/XML file.
    :returns list: A list containing first match in str.

    .. note::

        The whole line is returned if a match is found. And the tag is not validated.

