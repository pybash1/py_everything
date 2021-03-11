from setuptools import setup

readme_file = open("README.md", "r").read()


setup(
    name="py_everything",
    version="1.1.2",
    description="A python module containing all the basic functions and classes for python. From simple addition to advanced file encryption.",
    long_description=readme_file,
    long_description_content_type="text/markdown",
    author="play 4 Tutorials",
    author_email="play.4.tutotials@gmail.com",
    packages=['py_everything'],
    install_requires=['requests', 'pytube', 'playsound'],
    license="MIT License",
    url="https://github.com/play4Tutorials/py_everything/",
    repository="https://github.com/play4Tutorials/py_everything",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: Implementation :: CPython",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Communications :: Email",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Scientific/Engineering :: Mathematics",
    ],
    python_requires='>=3.6'
)
