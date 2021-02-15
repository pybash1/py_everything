from setuptools import setup

setup(
    name="py_utils",
    version="1.0.0",
    description="A python module containing all the basic functions and classes for python. From simple addition to advanced file encryption.",
    long_description=open("README.md", "r").read(),
    author="play 4 Tutorials",
    author_email="play.4.tutotials",
    packages=['py_utils'],
    install_requires=['requests'],
    license="MIT License",
    url="https://github.com/play4Tutorials/py_essentials",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.3'
)
