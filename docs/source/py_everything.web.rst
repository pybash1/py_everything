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

Function Name - google_search(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.google_search("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches Google for ``query``.

Search Youtube
--------------

Function Name - yt_search(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.yt_search("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches YouTube for ``query``.

Search GitHub
-------------

Function Name - github_search(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.github_search("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches GitHub for ``query``.

Search Stack Overflow
---------------------

Function Name - so_search(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.so_search("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches Stack Overflow for ``query``.

.. _search-amazonin:

Search Amazon.in
----------------

Function Name - amz_in_search(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.amz_in_search("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches Amazon.in for ``query``.

.. _search-amazoncom:

Search Amazon.com
-----------------

Function Name - amz_com_search(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.amz_com_search("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches Amazon.com for ``query``.

Search PyPI
-----------

Function Name - pypi_search(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.pypi_search("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches PyPI for ``query``.

Search Read The Docs
--------------------

Function Name - rtdocs_search(query)

No. of Parameters - 1

Parameters - query

Usage -
^^^^^^^

.. code:: python

   >>> pyeWeb.rtdocs_search("py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches Read the Docs for ``query``.

Search in a New Tab
-------------------

Function Name - open_new_tab(url, query)

No. of Parameters - 2

Parameters - url, query

Usage -
^^^^^^^

.. code:: python

   >>> google_url = 'https://google.com/search?q='
   >>> pyeWeb.open_new_tab(google_url, "py_everything")
   <--It opens a tab in your browser and shows the results-->

This function searches Google for ``query`` in a new tab.

Search in a New Window
----------------------

Function Name - open_new_window(url, query)

No. of Parameters - 2

Parameters - url, query

Usage -
^^^^^^^

.. code:: python

   >>> gh_url = 'https://github.com/search?q='
   >>> pyeWeb.open_new_window(gh_url, "py_everything")
   <--It opens a window in your browser and shows the results-->

This function searches GitHub for ``query`` in a new window.

... toctree::
   :caption: Basic:

.. toctree::
   :caption: Functions:

.. toctree::
   :caption: About the Project:
