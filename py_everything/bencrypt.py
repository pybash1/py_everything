from enrocrypt import encryption  # type: ignore
from typing import List


def encrypt(data: str):
    """Encrypts data"""
    value: List[bytes] = encryption.Encryption().Encrypt(bytes(data.encode()))
    return value


def decrypt(key: bytes, data: bytes):
    """Decrypts data"""
    value: bytes = encryption.Encryption().Decrypt(key, data)
    return str(value)


def listDecrypt(encryptedList: List[str]):
    """Decrypts data where encrypted data is given as a list"""
    value: bytes = encryption.Encryption().Decrypt_List(encryptedList)
    return str(value)


def encryptFile(filepath: str, keyFilepath: str):
    """Encrypts File"""
    return bool(encryption.Encryption().FileEncryption(filepath, keyFilepath))


def decryptFile(filepath: str, keyFilepath: str):
    """Decrypts File"""
    return bool(encryption.Encryption().FileDecryption(filepath, keyFilepath))
