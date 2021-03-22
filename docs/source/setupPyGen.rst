**********
setupPyGen
**********

Basic Usage:
============

.. code:: bash

   $ ls
   package/
   $ cd package/
   $ ls -a
   . ..
   $ setupPyGen -g True -t True --gitignore True
   <--Follow the prompts(packages entered - new, old)-->
   $ ls -a
   . .. .gitignore LICENSE README.md setup.py .git/ new/ old/ tests/
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

Flags:
======
There are different flags for setupPyGen. These flags take True or nothing.

* -g or --git
* -t or --tests
* --gitignore

All of these flags are optional. Rest of the data is taken input after running the command.

-g or --git
===========
The -g or --git flag is used to initialize a Git repository after the project structure and setup.py has been generated. It is usually
combined with the --gitignore falg for best results. 

--gitignore
===========
The --gitignore flag generates a .gitignore file in the project structure after everything else. It gives best results
when used with the -g or --git flag.

-t or --tests
=============
The -t or --tests flag is used to generate a tests directory in the project structure for unit tests.

Flags Usage:
=============
.. code:: bash

   $ setupPyGen -g True --tests True --gitignore True
   <--Folow the prompts(entered packages - new, old)-->
   $ ls -A
   .gitignore LICENSE README.md setup.py .git/ new/ old/ tests/ 

   $ setupPyGen -g True --gitignore True
   <--Folow the prompts(entered packages - new, old)-->
   $ ls -A
   .gitignore LICENSE README.md setup.py .git/ new/ old/

   $ setupPyGen -g True -t True
   <--Folow the prompts(entered packages - new, old)-->
   $ ls -A
   LICENSE README.md setup.py .git/ new/ old/ tests/

   $ setupPyGen
   <--Folow the prompts(entered packages - new, old)-->
   $ ls -A
   LICENSE README.md setup.py new/ old/

Note:
=====
setupPyGen, is a command-line utility seperate from the rest of the package.

It cannot be run using `$ python -m setupPyGen`. It gives an error. It can only be run using `$ setupPyGen`.

It's help utility can be accessed by using the command `$ setupPyGen -h` or `$setupPyGen --help`.

If you want to enable a flag just use "-flag True", for e.g., - `$ setupPyGen -t True`. All flags are disabled by default.

Do not disable flags manually, such as `$ setupPyGen -t False`, this still generates a tests/ directory.

.. toctree::
   :caption: Basic:

.. toctree::
   :caption: Functions:

.. toctree::
   :caption: setupPyGen:

.. toctree::
   :caption: About the Project:
