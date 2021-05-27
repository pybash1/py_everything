import os
import shutil
from . import error
def readFile(filePath: str):
    fileData = open(filePath, 'r').read()
    return fileData

def writeFile(filePath: str, writeData: str):
    if type(writeData) != type('str'):
        raise error.TypeError(type(writeData))
    with open(filePath, 'r+') as file:
        file.truncate(0)
        file.write(writeData)
        file.close()
        return True

def clearFile(filePath: str):
    with open(filePath, 'r+') as file:
        file.truncate(0)
        return True

def mkDir(dirName: str, path: str):
    if os.mkdir(os.path.join(path, dirName)):
        return True

def mkFile(fileName: str, path: str):
    with open(path+'\\'+fileName, 'w'): 
        pass
        return True

def delDir(path: str, dirName: str):
    if os.rmdir(os.path.join(path, dirName)):
        return True

def delDirRec(path: str, dirName: str):
    if shutil.rmtree(os.path.join(path, dirName)):
        return True

def delFile(path: str, fileName: str):
    if os.remove(os.path.join(path, fileName)):
        return True
