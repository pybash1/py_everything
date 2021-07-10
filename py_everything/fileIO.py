import os
import shutil

def readFile(filePath: str) -> str:
    fileData: str = open(filePath, 'r').read()
    return fileData

def writeFile(filePath: str, writeData: str) -> bool:
    if type(writeData) != type('str'):
        raise TypeError(f'Write Content Must Be Str Not {type(writeData)}')
    with open(filePath, 'r+') as file:
        file.truncate(0)
        file.write(writeData)
        file.close()
        return True

def clearFile(filePath: str) -> bool:
    with open(filePath, 'r+') as file:
        file.truncate(0)
        return True

def mkDir(dirName: str, path: str):
    os.mkdir(os.path.join(path, dirName))

def mkFile(fileName: str, path: str):
    with open(path+'\\'+fileName, 'w'): 
        pass

def delDir(path: str, dirName: str):
    os.rmdir(os.path.join(path, dirName))

def delDirRec(path: str, dirName: str):
    shutil.rmtree(os.path.join(path, dirName))

def delFile(path: str, fileName: str):
    os.remove(os.path.join(path, fileName))
