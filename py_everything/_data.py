setupPyData = '''from setuptools import setup

readme_file = open("{}", "r").read()

setup(
    name="{}",
    version="{}",
    description="{}",
    long_description=readme_file,
    long_description_content_type="text/markdown",
    author="{}",
    author_email="{}",
    packages={},
    install_requires={},
    license="{}",
    url="{}",
    python_requires="{}"
)
'''

help_desc='''
setupPyGen {} Help Utility
------------------------------
Welcome to help utility for setupPyGen. setupPyGen is a command-line utility to generate a python package project structure for you. Including setup.py

It has very few command-line arguments, most data is taken input after running, the command "setupPyGen" in the directory where you want to generate you python package project structure.

You are currently using setupPyGen {}, with Python {}.
'''
