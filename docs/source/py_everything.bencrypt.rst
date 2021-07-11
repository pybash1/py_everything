*****************************
:mod:`py_everything.bencrypt`
*****************************

.. module:: py_everything.bencrypt

**Source code:** `py_everything/bencrypt.py <https://github.com/pybash1/py_everything/blob/master/py_everything/bencrypt.py>`_

This module deals with encryption using the `enrocrypt <https://github.com/Morgan-Phoenix/EnroCrpyt>`_ library

.. versionadded:: 2.1.0

.. function:: encrypt(data)

Returns List containing specially formatted encrypted data for ``data``.

:returns List: List containing specially formatted encrypted data for ``data``

.. function:: decrypt(key, data)

Returns decrypted data using ``key``.

:returns bytes: Str/bytes containing decrypted data using key.

.. note:: This requires you to provide the key and data separately in 2 arguments from the encrypted List.

.. function:: listDecrypt(encryptedList)

Returns decrypted data using key from ``encryptedList``.

:returns bytes: Str/bytes containing decrypted data using key.

.. function:: encryptFile(filepath, keyFilepath)

Returns bool depending on encryption successful or not.

:returns bool: True if encryption successful, Flase if not

.. function:: decryptFile(filepath, keyFilepath)

Returns bool depending on decryption successful or not.

:returns bool: True if decryption successful, Flase if not
