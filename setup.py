from setuptools import setup

setup(
    name="py_everything",
    version="1.1.0",
    description="A python module containing all the basic functions and classes for python. From simple addition to advanced file encryption.",
    long_description=open("README.md", "r").read(),
    author="play 4 Tutorials",
    author_email="play.4.tutotials@gmail.com",
    packages=['py_everything'],
    install_requires=['requests', 'pytube', 'playsound'],
    license="MIT License",
    url="https://github.com/play4Tutorials/py_everything",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: Implementation :: CPython",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    python_requires='>=3.5'
)
