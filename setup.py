from setuptools import setup, find_packages

readme_file = open("README.md", "r").read()


setup(
    name="py_everything",
    version="2.3.0",
    description="A python module containing all the basic functions and classes for python but doesn't stop at that, goes beyond advanced. From simple addition to advanced file encryption.",
    long_description=readme_file,
    long_description_content_type="text/markdown",
    author="PyBash",
    maintainer="PyBash",
    packages=find_packages(),
    entry_points={
            'console_scripts': [
                'setupPyGen = py_everything.setupPyGen:main',
                'gitIt = py_everything.gitIt:main',
            ]
    },
    install_requires=['requests', 'playsound', 'setuptools',
                      'wheel', 'pip', 'enrocrypt', 'py-expression-eval'],
    license="MIT License",
    url="https://github.com/pybash1/py_everything",
    download_url="https://pypi.org/project/py-everything/#files",
    project_urls={'Documentation': 'https://py_everything.readthedocs.io/en/stable/',
                  'Issues': 'https://github.com/pybash1/py_everything/issues',
                  'Code': 'https://github.com/pybash1/py_everything/'
                  },
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
        "Topic :: Multimedia :: Video",
        "Topic :: Scientific/Engineering :: Physics",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Security :: Cryptography",
        "Topic :: Utilities",
        "Topic :: System :: Installation/Setup",
        "Topic :: System :: Archiving :: Packaging",
        "Topic :: Software Development :: Code Generators",
    ],
    python_requires='>=3.6'
)
