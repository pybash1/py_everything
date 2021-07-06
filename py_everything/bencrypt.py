# from enrocrypt import encryption
# from typing import List

# def encrypt(data: str):
#     value = encryption.Encryption().Encrypt(bytes(data.encode()))
#     return value

# def decrypt(key: bytes, data: bytes):
#     value = encryption.Encryption().Decrypt(key,data)
#     return value

# def listDecrypt(encryptedList: List[str]):
#     value = encryption.Encryption().Decrypt_List(encryptedList)
#     return value

# def encryptFile(filepath: str, keyFilepath: str):
#     if encryption.Encryption().FileEncryption(filepath, keyFilepath):
#         return True
#     else:
#         return False

# def decryptFile(filepath: str, keyFilepath: str):
#     if encryption.Encryption().FileDecryption(filepath, keyFilepath):
#         return True
#     else:
#         return False
