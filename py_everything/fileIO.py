import os
import shutil

def readFile(filePath: str) -> str:
    '''Returns data presend in a file'''
    with open(filePath, 'r') as f:
        fileData: str = f.read()
    return fileData

def writeFile(filePath: str, writeData: str) -> bool:
    '''Writes given data to given file'''
    if type(writeData) != type('str'):
        raise TypeError(f'Write Content Must Be Str Not {type(writeData)}')
    with open(filePath, 'r+') as file:
        file.truncate(0)
        file.write(writeData)
        file.close()
        return True

def clearFile(filePath: str) -> bool:
    '''Clears contents of a file'''
    with open(filePath, 'r+') as file:
        file.truncate(0)
        return True

def mkDir(dirName: str, path: str):
    '''Creates a directory'''
    os.mkdir(os.path.join(path, dirName))

def mkFile(fileName: str, path: str):
    '''Creates a file'''
    with open(path+'\\'+fileName, 'w'): 
        pass

def delDir(path: str, dirName: str):
    '''Deletes a directory'''
    os.rmdir(os.path.join(path, dirName))

def delDirRec(path: str, dirName: str):
    '''Deletes a directory recursively'''
    shutil.rmtree(os.path.join(path, dirName))

def delFile(path: str, fileName: str):
    '''Deletes a file'''
    os.remove(os.path.join(path, fileName))
