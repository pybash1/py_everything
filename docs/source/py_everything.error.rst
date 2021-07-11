***************************
:mod:`py_everything.error`
***************************

.. module:: py_everything.error

**Source code:** `py_everything/error.py <https://github.com/pybash1/py_everything/blob/master/py_everything/error.py>`_

.. class:: pycacheNotFoundError()

    Exception raised when `__pycache__` is not found.

.. class:: instalModulesFailedError()

    Exception raised when modules can't be installed successfully and fails.

.. class:: startAppFailedError()

    Exception raised when exe launch fails.

.. class:: InvalidKeyListError()

    Exception raised when key list is invalid in ``sencrypt``.

    .. versionadded:: 2.0.0

.. class:: InvalidSymbolKeyError()

    Exception raised when symbol key is invalid in ``sencrypt``.

    .. versionadded:: 2.0.0

.. class:: InvalidOperationPerformedError()

    Exception raised when unsupported operation is performed on a path

    .. versionadded:: 2.1.0

.. class:: UnknownPathTypeError()

    Exception raised when path type can't be determined

    .. versionadded:: 2.1.0

.. class:: UnknownDivisionTypeError()

    Exception raised when division type can't be determined

    .. versionadded:: 2.1.0
