.. sectionauthor:: Play 4 Tutorials <play.4.tutotials@gmail.com>

.. _py_everything: http://github.com/play4Tutorials/py_everything
.. _Python: http://www.python.org/

******************************************
Welcome to py_everything_'s Documentation!
******************************************

Welcome to the Documentation for py_everything_.
You can find all the modules and how to use them here.

py_everything_ hopes to become a Python_ package that helps you write **everything** much faster and in a easier way.

Power of py_everything_ - 
^^^^^^^^^^^^^^^^^^^^^^^^^

The basic usage for this package is given below::

   >>> import py_everything
   >>> from py_everything import search
   >>> search.search_files('python', 'C:\Programming\\')
   C:\Programming\python.txt
   C:\Programming\projectpython.py
   C:\Programming\py_everything-python.docx
   >>> my_list = [2, 4, 5, 3, 7, 5, 6, 3 , 12 , 9, 6]
   >>> py_everything.maths.avg(my_list)
   5.636363636363637


Contributors - 
^^^^^^^^^^^^^^

People who have contributed to this project - 

* `Play 4 Tutorials(Creator and Maintainer) <https://github.com/play4Tutorials>`_


.. toctree::
   :caption: Basic:
   :maxdepth: 2
   
   index
   Modules, Functions, and Classes
   glossary

.. toctree::
   :caption: Functions:
   :maxdepth: 2
   
   py_everything
   py_everything.automation
   py_everything.date_utils
   py_everything.fileIO
   py_everything.maths
   py_everything.requestsLib
   py_everything.search
   py_everything.web

.. toctree::
   :caption: About the Project:
   :maxdepth: 2
   
   Dependencies & Dependents
   License


.. 
   Indices
   =======
   * :ref:`genindex`
