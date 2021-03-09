*************************
py_everything.requestsLib
*************************

Import -
--------

How to import the module?

.. code:: python

   >>> import py_everything.requestsLib as pyeRLib

Send a GET Request
------------------

Function Name - getR(apiUrl)

No. of Parameters - 1

Parameters - apiUrl

Usage -
^^^^^^^

.. code:: python

   >>> pyeRLib.getR("protocol://api.domain.com/user/1")
   <Response [200]>

This function uses `requests`_ to send a get request to ``apiUrl``.

Send a POST Request
-------------------

Function Name - postR(apiUrl, data=None)

No. of Parameters - 2

Parameters - apiUrl, data

Usage -
^^^^^^^

.. code:: python

   >>> pyeRLib.postR("protocol://api.domain.com/users", "{\"id\":1}")
   <Response [200]>

This function uses `requests`_ to send a post request to ``apiUrl``.

Send a PUT Request
------------------

Function Name - putR(apiUrl, data=None)

No. of Parameters - 2

Parameters - apiUrl, data

Usage -
^^^^^^^

.. code:: python

   >>> pyeRLib.putR("protocol://api.domain.com/users", data="{\"id\":1")
   <Response [200]>

This function uses `requests`_ to send a put request to ``apiUrl``.

Send a DELETE Request
---------------------

Function Name - deleteR(apiUrl)

No. of Parameters - 1

Parameters - apiUrl

Usage -
^^^^^^^

.. code:: python

   >>> pyeRLib.deleteR("protocol://api.domain.com/user/1")
   <Response [200]>

This function uses `requests`_ to send a delete request to ``apiUrl``.

Send a PATCH Request
--------------------

Function Name - patchR(apiUrl, data=None)

No. of Parameters - 2

Parameters - apiUrl, data

Usage -
^^^^^^^

.. code:: python

   >>> pyeRLib.patchR("protocol://api.domain.com/users", data="\"id\":1")
   <Response [200]>

This function uses `requests`_ to send a patch request to ``apiUrl``.

Send a OPTIONS Request
----------------------

Function Name - optionsR(apiUrl)

No. of Parameters - 1

Parameters - apiUrl

Usage -
^^^^^^^

.. code:: python

   >>> pyeRLib.optionsR("protocol://api.domain.com/users")
   <Response [200]>

This function uses `requests`_ to send a options request to ``apiUrl``.

Send a HEAD Request
-------------------

Function Name - headR(apiUrl)

No. of Parameters - 1

Parameters - apiUrl

Usage -
^^^^^^^

.. code:: python

   >>> pyeRLib.headR("protocol://api.domain.com/users")
   <Response [200]>

This function uses `requests`_ to send a head request to ``apiUrl``.

Get Content from a Response
---------------------------

Function Name - getContent(response)

No. of Parameters - 1

Parameters - response

Usage -
^^^^^^^

.. code:: python

   >>> pyeRLib.getContent(pyeRLib.getR("protocol://api.domain.com/user/1"))
   <--Content of the reponse-->

This function uses `requests`_ to get the content of ``response``.

Get Text from a Response
------------------------

Function Name - getText(response)

No. of Parameters - 1

Parameters - response

Usage -
^^^^^^^

.. code:: python

   >>> pyeRLib.getText(pyeRLib.getR("protocol://api.domain.com/user/1"))
   <--Text of the reponse-->

This function uses `requests`_ to get the text returned to ``response``.

Get JSON from a Response
------------------------

Function Name - getJson(response)

No. of Parameters - 1

Parameters - response

Usage -
^^^^^^^

.. code:: python

   >>> pyeRLib.getJson(pyeRLib.getR("protocol://api.domain.com/user/1"))
   <--JSON of the reponse-->

This function uses `requests`_ to get the JSON returned to ``response``.

Get Headers from a Response
---------------------------

Function Name - getHeader(response)

No. of Parameters - 1

Parameters - response

Usage -
^^^^^^^

.. code:: python

   >>> pyeRLib.getHeader(pyeRLib.getR("protocol://api.domain.com/user/1"))
   <--Headers of the reponse-->

This function uses `requests`_ to get the Headers returned to
``response``.

Get a Specific Header from a Response
-------------------------------------

Function Name - getSpecificHeader(response, headerName)

No. of Parameters - 2

Parameters - response, headerName

Usage -
^^^^^^^

.. code:: python

   >>> pyeRLib.getSpecificHeader(pyeRLib.getR("protocol://api.domain.com/user/1"))
   <--Content of headerName of the reponse-->

This function uses `requests`_ to get the content of ``headerName``
returned to ``response``.

.. _requests: https://requests.readthedocs.io

.. toctree::
   :caption: Basic:

.. toctree::
   :caption: Functions:

.. toctree::
   :caption: About the Project:
