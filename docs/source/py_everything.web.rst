*****************
py_everything.web
*****************

Import -
--------

How to import the module?

.. code:: python

   >>> import py_everything.web as pyeWeb

Search Google
-------------

Function Name - googleSearch(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.googleSearch("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches Google for ``query``.

Search Youtube
--------------

Function Name - ytSearch(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.ytSearch("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches YouTube for ``query``.

Search GitHub
-------------

Function Name - githubSearch(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.githubSearch("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches GitHub for ``query``.

Search Stack Overflow
---------------------

Function Name - soSearch(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.soSearch("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches Stack Overflow for ``query``.

.. _search-amazonin:

Search Amazon.in
----------------

Function Name - amzInSearch(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.amzInSearch("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches Amazon.in for ``query``.

.. _search-amazoncom:

Search Amazon.com
-----------------

Function Name - amzComSearch(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.amzComSearch("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches Amazon.com for ``query``.

Search PyPI
-----------

Function Name - pypiSearch(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.pypiSearch("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches PyPI for ``query``.

Search Read The Docs
--------------------

Function Name - rtdocsSearch(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.rtdocsSearch("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches Read the Docs for ``query``.

Search in a New Tab
-------------------

Function Name - openNewTab(url, query)

No. of Parameters - 2

Parameters - url, query

Usage -
^^^^^^^

.. code:: python

   >>> google_url = 'https://google.com/search?q='
   >>> pyeWeb.openNewTab(google_url, "py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches Google for ``query`` in a new tab.

Search in a New Window
----------------------

Function Name - openNewWindow(url, query)

No. of Parameters - 2

Parameters - url, query

Usage -
^^^^^^^

.. code:: python

   >>> gh_url = 'https://github.com/search?q='
   >>> pyeWeb.openNewWindow(gh_url, "py_everything")
   <--It opens a window in your browser and shows the results-->

This function searches GitHub for ``query`` in a new window.

.. toctree::
   :caption: Basic:

.. toctree::
   :caption: Functions:

.. toctree::
   :caption: setupPyGen:

.. toctree::
   :caption: About the Project:
