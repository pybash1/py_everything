from enrocrypt import encryption #type: ignore
from typing import List

def encrypt(data: str):
    value: List[bytes] = encryption.Encryption().Encrypt(bytes(data.encode()))
    return value

def decrypt(key: bytes, data: bytes):
    value: bytes = encryption.Encryption().Decrypt(key, data)
    return str(value)

def listDecrypt(encryptedList: List[str]):
    value: bytes = encryption.Encryption().Decrypt_List(encryptedList)
    return str(value)

def encryptFile(filepath: str, keyFilepath: str):
    if encryption.Encryption().FileEncryption(filepath, keyFilepath):
        return True
    return False

def decryptFile(filepath: str, keyFilepath: str):
    if encryption.Encryption().FileDecryption(filepath, keyFilepath):
        return True
    return False
