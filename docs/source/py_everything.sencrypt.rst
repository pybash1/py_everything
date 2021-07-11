******************************
:mod:`py_everything.sencrypt`
******************************

.. module:: py_everything.sencrypt

**Source code:** `py_everything/sencrypt.py <https://github.com/pybash1/py_everything/blob/master/py_everything/sencrypt.py>`_

This module deals with Encryption. Currently only string
encryption is supported but file encryption will be supported soon.

.. function:: genCharKeys()

    This generates 4 character keys and returns the list
    containing them. These keys are required for encryption.

    :returns list: List of keys for encryption

.. function:: genSymKey()

    This generates a symbol key and returns the same. These keys are required for encryption.

    :returns str: Symbol key for encryption

.. function:: checkCharKeys(keyList)

    Checks if character keys are valid.

    :param keyList: List of keys
    :raises error.InvalidKeyListError: Raised when ``keyList`` contains invalid.

.. function:: checkSymKey(symKey)

    Checks if symbol key is valid.

    :param symKey: Symbol key
    :raises error.InvalidSymbolKeyError: Raised when ``symKey`` is invalid.

.. class:: SuperEncrypt(keyCharLsit, keySym)

    This class creates a ``SuperEncrypt()`` object to encrypt and decrypt using keys.

    .. code::
    
        >>> from py_everything.sencrypt import SuperEncrypt
        >>> import py_everything.sencrypt as se
        >>> charKeys = se.genCharKeys()
        >>> symbolKey = se.genSymKey()
        >>> seObj = SuperEncrypt(charKeys, symbolKey)
        >>> text = 'my super secret text'
        >>> encrypted = seObj.encrypt(text)
        >>> encrypted
        '...'
        >>> decrypted = seObj.decrypt(encrypted)
        >>> decrypted
        'my super secret text'

    :param keyCharList: List of character keys
    :param str keySym: Symbolkeys

    .. function:: encrypt(msg)

        Encrypts ``msg`` using provided keys.

        :param str msg: Text to be encrypted.
        :returns str: Encrypted string.

    .. function:: decrypt(msg)

        Decrypts ``msg`` using provided keys.

        :param str msg: String to be decrypted.
        :returns str: Decrypted text.
