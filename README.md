# py_everything

A python module containing all the functions and classes from basic to advanced for Python. From simple calculations  to advanced file encryption. **Everything** is included in this one package.

It allows you to use all of its functions and classes without having to write huge complex code. It is a very simple and easy to use library. 

# Installation

py_everything is available on [PyPi](https://pypi.org/project/py_everything), and you can install it as follows:

```
$ python -m pip install py_everything
```
py_everything officially supports Python 3.5+

# Features

- You can make use of the thousands of functions and classes available to you.
- Simple and easy to use
- You don't have to write all of that code yourself, just call the pre-made functions.
- You can inherit from our base class, and make your own with customizations.
- There are two variants of most classes, a `Base` variant and an `Advanced` variant.
- Make your own classes from our pre-provided `Base` variants. The Advanced ones are not for inheriting, but there is no problem in experimenting.

# Documentation and Usage

The documentation can be found on [GitHub](https://github.com/play4Tutorials/py_everything/tree/master/docs)


The basic usage for this library is given below:

```python
>>> import py_everything
>>> from py_everything import search
>>> search.search_files('python', 'C:\Programming\\')
C:\Programming\python.txt
C:\Programming\python_project.py
C:\Programming\python_py_everything.docx
>>> my_list = [2, 4, 5, 3, 7, 5, 6, 3 , 12 , 9, 6]
>>> py_everything.maths.avg(my_list)
5.636363636363637
```

# Contributing

For details, on how to contribute, please read [CONTRIBUTING.md](https://github.com/play4Tutorials/py_everything/tree/master/CONTRIBUTING.md)
