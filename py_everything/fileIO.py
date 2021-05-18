import os
import shutil

def readFile(fileName):
    fileData = open(fileName, 'r').read()
    return fileData

def writeFile(fileName, writeData):
    with open(fileName, 'r+') as file:
        file.truncate(0)
        file.write(writeData)
        file.close()
        return True

def clearFile(fileName):
    with open(fileName, 'r+') as file:
        file.truncate(0)
        return True

def mkDir(dirName, path):
    if os.mkdir(os.path.join(path, dirName)):
        return True

def mkFile(fileName, path):
    with open(path+'\\'+fileName, 'w'): 
        pass
        return True

def delDir(path, dirName):
    if os.rmdir(os.path.join(path, dirName)):
        return True

def delDirRec(path, dirName):
    if shutil.rmtree(os.path.join(path, dirName)):
        return True

def delFile(path, fileName):
    if os.remove(os.path.join(path, fileName)):
        return True
