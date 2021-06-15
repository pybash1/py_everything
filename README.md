<p align="center">

<img width="170px" height="170px" src="https://raw.githubusercontent.com/play4Tutorials/py_everything/master/extra/logo.png" alt="Logo">

</p>

# py_everything

A python module containing all the functions and classes from basic to advanced for Python. From simple calculations  to advanced file encryption. **Everything** is included in this one package.

It allows you to use all of its functions and classes without having to write huge complex code. It is a very simple and easy to use library. 

Downloads - 

[![Downloads](https://pepy.tech/badge/py-everything)](https://pypi.org/project/py-everything)
[![Downloads](https://pepy.tech/badge/py-everything/month)](https://pypi.org/project/py-everything)
[![Downloads](https://pepy.tech/badge/py-everything/week)](https://pypi.org/project/py-everything)

PyPI - 

[![PyPI - Implementation](https://img.shields.io/pypi/implementation/py-everything?logo=python&logoColor=yellow)](https://pypi.org/project/py-everything)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/py-everything?logo=pypi&logoColor=green)](https://pypi.org/project/py-everything)
[![PyPI](https://img.shields.io/pypi/v/py-everything?logo=pypi&logoColor=green)](https://pypi.org/project/py-everything)
[![PyPI - Wheel](https://img.shields.io/pypi/wheel/py-everything)](https://pypi.org/project/py-everything)
[![PyPI - Status](https://img.shields.io/pypi/status/py-everything)](https://pypi.org/project/py-everything)
[![PyPI - License](https://img.shields.io/pypi/l/py-everything?color=success)](https://pypi.org/project/py-everything)

Status - 

[![Libraries.io dependency status for latest release](https://img.shields.io/librariesio/release/pypi/py-everything/1.1.1)](https://libraries.io/pypi/py-everything)
[![GitHub issues](https://img.shields.io/github/issues/play4Tutorials/py_everything)](https://github.com/play4Tutorials/py_everything/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/play4Tutorials/py_everything)](https://github.com/play4Tutorials/py_everything/pulls)
[![GitHub branch checks state](https://img.shields.io/github/checks-status/play4Tutorials/py_everything/master)](https://github.com/play4Tutorials/py_everything)
[![GitHub Workflow Status](https://img.shields.io/github/workflow/status/play4Tutorials/py_everything/Test%20Package)](https://github.com/play4Tutorials/py_everything)
[![Documentation Status](https://readthedocs.org/projects/py-everything/badge/?version=latest)](https://py-everything.readthedocs.io/en/latest/?badge=latest)

GitHub - 

[![GitHub forks](https://img.shields.io/github/forks/play4Tutorials/py_everything?style=social)](https://github.com/play4Tutorials/py_everything/pulls)
[![GitHub Repo stars](https://img.shields.io/github/stars/play4Tutorials/py_everything?style=social)](https://github.com/play4Tutorials/py_everything/pulls)
[![GitHub watchers](https://img.shields.io/github/watchers/play4Tutorials/py_everything?style=social)](https://github.com/play4Tutorials/py_everything/pulls)
[![GitHub repo size](https://img.shields.io/github/repo-size/play4Tutorials/py_everything?logo=github)](https://github.com/play4Tutorials/py_everything/pulls)

Discord - 

https://cdn.jsdelivr.net/npm/simple-icons@v4/icons/discord.svg(https://discord.gg/DUeaUDxC7t)

# Installation

py_everything is available on [PyPi](https://pypi.org/project/py-everything), and you can install it as follows:

`$ python -m pip install py-everything`

py_everything officially supports Python 3.6+

# Features

- You can make use of the huge number of functions and classes available to you.
- Has an in-built CLI tool that generates a python package project structure for you. - setupPyGen
- setupPyGen now comes with support for `find_packages()`
- Now come with a second CLI tool - gitIt for generating GitHub friendly project structures
- Good and Consistent Naming Convention. - Camel Case
- Simple and easy to use.
- You don't have to write all of that code yourself, just call the pre-made functions.
- Now comes with usefull classes.

# setupPyGen

Detailed documentation can be found on [ReadTheDocs](https://py-everything.readthedocs.io/en/latest/setupPyGen.html)

Basic Usage:

```bash
$ ls
package/ new/ old/
$ cd package/
$ ls -a
. ..
$ setupPyGen -g True -t True --gitignore True
<--Follow the prompts(packages entered - new, old)-->
$ ls -A
.gitignore LICENSE README.md setup.py .git/ new/ old/ tests/
$ cat setup.py
from setuptools import setup

readme_file = open("README.md", "r").read()


setup(
    name="package-name",
    version="1.0.0",
    description="Given Project Description",
    long_description=readme_file,
    long_description_content_type="text/markdown",
    author="Author Name",
    author_email="name@example.com",
    packages=[new, old],
    install_requires=[],
    license="MIT License",
    url="https://github.com/play4Tutorials/py_everything/",
    python_requires='>=3.5'
)
```

NOTE: Currently setupPyGen doesn't support classifiers. But support will be added soon. `find_packages()` support has been added.

# gitIt

Detailed documentation can be found on [ReadTheDocs](https://py-everything.readthedocs.io/en/latest/gitIt.html)

Basic Usage:

```bash
$ ls
project1/ project2/
$ cd project1/
$ ls -a
. ..
$ gitIt -gh -s -i -c --greet
<--Follow the prompts(packages entered - new, old)-->
$ ls -A
.github/ .gitignore LICENSE README.md .git/ 
$ cd .github/
$ ls -A
SECURITY.md workflows/ ISSUE_TEMPLATE/
$ cd workflows/
$ ls -A
greet.yml
$ cd ..
$ cd ISSUE_TEMPLATE/
$ ls
bug-report.md feature-or-enhancement-request.md
$ cd ../..
$ echo "Note that all of these files also have data in it they are not empty!"
Note that all of these files also have data in it they are not empty!
```

# Documentation and Usage

The documentation can be found on [ReadTheDocs](https://py-everything.readthedocs.io/en/latest/)


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
