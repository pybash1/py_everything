from typing import List

'''
Super Encrypt - Encryption Algorithm with 4 key encryption and decryption

__author__ = "PyBash"
__version__ = "v1.0.0"
'''
import random
from . import error

BASE_LETTERS: str = 'abcdefghijklmnopqrstuvwxyz'
BASE_SYMBOLS: str = ' 1234567890!@#$%^&*()-_=+[{]};:\'"<,>.?/`~|\\'

def genCharKeys() -> List[str]:
    base: List[str] = list(BASE_LETTERS)
    random.shuffle(base)
    key1 = ''.join(base)
    random.shuffle(base)
    key2 = ''.join(base)
    random.shuffle(base)
    key3 = ''.join(base)
    random.shuffle(base)
    key4 = ''.join(base)
    keyList: List[str] = []
    keyList.append(key1)
    keyList.append(key2)
    keyList.append(key3)
    keyList.append(key4)
    return keyList

def genSymKey() -> str:
    base: List[str] = list(BASE_SYMBOLS)
    random.shuffle(base)
    key: str = ''.join(base)
    return key

def checkCharKeys(keyList: List[str]):
    key1 = keyList[0].replace("\n", '')
    key2 = keyList[1].replace("\n", '')
    key3 = keyList[2].replace("\n", '')
    key4 = keyList[3].replace("\n", '')
    base = BASE_LETTERS
    key1Sorted: List[str] = sorted(key1)
    key2Sorted: List[str] = sorted(key2)
    key3Sorted: List[str] = sorted(key3)
    key4Sorted: List[str] = sorted(key4)
    baseSorted: List[str] = sorted(base)
    key1 = "".join(key1Sorted)
    key2 = "".join(key2Sorted)
    key3 = "".join(key3Sorted)
    key4 = "".join(key4Sorted)
    base = "".join(baseSorted)
    
    if key1 != base:
        raise error.InvalidKeyListError()
    elif key2 != base:
        raise error.InvalidKeyListError()
    elif key3 != base:
        raise error.InvalidKeyListError()
    elif key4 != base:
        raise error.InvalidKeyListError()
    
def checkSymKey(symKey: str): 
    sym: str = symKey
    base: str = BASE_SYMBOLS
    symSorted: List[str] = sorted(sym)
    baseSorted: List[str] = sorted(base)
    sym = "".join(symSorted)
    base = "".join(baseSorted)
    
    if sym != base:
        raise error.InvalidSymbolKeyError()

class SuperEncrypt():
    def __init__(self, keyCharList: List[str], keySym: str):
        self.keyCharList: List[str] = keyCharList
        self.key1 = self.keyCharList[0]
        self.key2 = self.keyCharList[1]
        self.key3 = self.keyCharList[2]
        self.key4 = self.keyCharList[3]
        self.key5: str = keySym

    def encrypt(self, msg: str) -> str:
        encrypted1: str = ''
        encrypted2: str = ''
        encrypted3: str = ''
        encrypted4: str = ''
        encryptedSym: str = ''
        
        checkCharKeys(self.keyCharList)
        checkSymKey(self.key5)
        
        for char in msg:
            actualChars: str = BASE_LETTERS
            encryptedChars: str = self.key1
            if char.lower() not in actualChars:
                encrypted1 += char.replace(char, char)
            else:
                charIndex: int = actualChars.find(char.lower())
                encryptedElem: str = encryptedChars[charIndex]
                if char.isupper():
                    encrypted1 += char.replace(char, encryptedElem.upper())
                else:
                    encrypted1 += char.replace(char, encryptedElem)
        
        for char in encrypted1:
            actualChars = BASE_LETTERS
            encryptedChars = self.key2
            if char.lower() not in actualChars:
                encrypted2 += char.replace(char, char)
            else:
                charIndex = actualChars.find(char.lower())
                encryptedElem = encryptedChars[charIndex]
                if char.isupper():
                    encrypted2 += char.replace(char, encryptedElem.upper())
                else:
                    encrypted2 += char.replace(char, encryptedElem)
        
        for char in encrypted2:
            actualChars = BASE_LETTERS
            encryptedChars = self.key3
            if char.lower() not in actualChars:
                encrypted3 += char.replace(char, char)
            else:
                charIndex = actualChars.find(char.lower())
                encryptedElem = encryptedChars[charIndex]
                if char.isupper():
                    encrypted3 += char.replace(char, encryptedElem.upper())
                else:
                    encrypted3 += char.replace(char, encryptedElem)
        
        for char in encrypted3:
            actualChars = BASE_LETTERS
            encryptedChars = self.key4
            if char.lower() not in actualChars:
                encrypted4 += char.replace(char, char)
            else:
                charIndex = actualChars.find(char.lower())
                encryptedElem = encryptedChars[charIndex]
                if char.isupper():
                    encrypted4 += char.replace(char, encryptedElem.upper())
                else:
                    encrypted4 += char.replace(char, encryptedElem)
        
        for char in encrypted4:
            actualChars = BASE_SYMBOLS
            encryptedChars = self.key5
            if char.lower() not in actualChars:
                encryptedSym += char.replace(char, char)
            else:
                charIndex = actualChars.find(char.lower())
                encryptedElem = encryptedChars[charIndex]
                if char.isupper():
                    encryptedSym += char.replace(char, encryptedElem.upper())
                else:
                    encryptedSym += char.replace(char, encryptedElem)
        
        return encryptedSym

    def decrypt(self, msg: str) -> str:
        decrypted4: str = ''
        decrypted3: str = ''
        decrypted2: str = ''
        decrypted1: str = ''
        decryptedSym: str = ''
        
        checkCharKeys(self.keyCharList)
        checkSymKey(self.key5)
        
        for char in msg:
            actualChars = self.key4
            decryptedChars: str = BASE_LETTERS
            if char.lower() not in actualChars:
                decrypted4 += char.replace(char, char)
            else:
                charIndex = actualChars.find(char.lower())
                decryptedElem: str = decryptedChars[charIndex]
                if char.isupper():
                    decrypted4 += char.replace(char, decryptedElem.upper())
                else:
                    decrypted4 += char.replace(char, decryptedElem)
        
        for char in decrypted4:
            actualChars = self.key3
            decryptedChars = BASE_LETTERS
            if char.lower() not in actualChars:
                decrypted3 += char.replace(char, char)
            else:
                charIndex = actualChars.find(char.lower())
                decryptedElem = decryptedChars[charIndex]
                if char.isupper():
                    decrypted3 += char.replace(char, decryptedElem.upper())
                else:
                    decrypted3 += char.replace(char, decryptedElem)
        
        for char in decrypted3:
            actualChars = self.key2
            decryptedChars = BASE_LETTERS
            if char.lower() not in actualChars:
                decrypted2 += char.replace(char, char)
            else:
                charIndex = actualChars.find(char.lower())
                decryptedElem = decryptedChars[charIndex]
                if char.isupper():
                    decrypted2 += char.replace(char, decryptedElem.upper())
                else:
                    decrypted2 += char.replace(char, decryptedElem)
        
        for char in decrypted2:
            actualChars = self.key1
            decryptedChars = BASE_LETTERS
            if char.lower() not in actualChars:
                decrypted1 += char.replace(char, char)
            else:
                charIndex = actualChars.find(char.lower())
                decryptedElem = decryptedChars[charIndex]
                if char.isupper():
                    decrypted1 += char.replace(char, decryptedElem.upper())
                else:
                    decrypted1 += char.replace(char, decryptedElem)
        
        for char in decrypted1:
            actualChars = self.key5
            decryptedChars = BASE_SYMBOLS
            if char.lower() not in actualChars:
                decryptedSym += char.replace(char, char)
            else:
                charIndex = actualChars.find(char.lower())
                decryptedElem = decryptedChars[charIndex]
                if char.isupper():
                    decryptedSym += char.replace(char, decryptedElem.upper())
                else:
                    decryptedSym += char.replace(char, decryptedElem)

        return decryptedSym
