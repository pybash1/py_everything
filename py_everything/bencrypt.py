from enrocrypt import *

def encrypt(Data:str):
    value = encryption.Encrypt(bytes(Data.encode()))
    return value

def decrypt(Key:bytes,Data:bytes):
    value = encryption.Decrypt(Key,Data)
    return value

def listDecrypt(List:list):
    value = encryption.Decrypt_List(List)
    return value

def encryptFile(Filepath:str,Keyfilepath:str):
    encryption.FileEncryption(Filepath,Keyfilepath)
    return None

def decryptFile(Filepath:str,Keyfilepath:str):
    encryption.FileDecryption(Filepath,Keyfilepath)
    return None
