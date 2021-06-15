from enrocrypt import *
def encrypt(Data:str): #Tested OK
    '''This Function Encrypts Data That is Given. Accepts one Argument with type str'''
    value = encryption.Encrypt(bytes(Data.encode()))
    return value
def decrypt(Key:bytes,Data:bytes): #Tested OK
    '''This Function Decrypts The Data Encrypted By Encrypt(). Accepts Two Arguments, Key as bytes(The Value That Is Pointed In The List As Key) and Data (The Bytes Value Pointed By Encrypted_Data in The List)'''
    value = encryption.Decrypt(Key,Data)
    return value
def listDecrypt(List:list): #Tested OK
    '''Decrypts The List Provided By Encrypt() (You Don't Have To Remove Anything).
    Just Pass The List Returned By Encrypt()'''
    value = encryption.Decrypt_List(List)
    return value
def encryptFile(Filepath:str,Keyfilepath:str): #Tested OK
    '''Make Sure The Path You Give Has "\\" insted of just "\". KeyFilePath Takes the path where you have to keep the key for the encrypted file, Path Takes the path of the file which has to be encrypted
    Warning: You Can Use The Key File To Store Multiple Keys But The Keys Must Not Be of The Same File Else You Will Get A Invalid Key Error And You Will Lose Your Data''' # Please Modify This As I Pasted The Exact Doc string That Is There In My Module For The FileEncryption Function
    encryption.FileEncryption(Filepath,Keyfilepath)
    return None
def decryptFile(Filepath:str,Keyfilepath:str): #Tested OK
    '''Filepath: The Path Of The Encrypted File
    KeyFilePath: Path Of That key File Where The Decryption Key Is Stored For The File ''' # same as above
    encryption.FileDecryption(Filepath,Keyfilepath)
    return None
