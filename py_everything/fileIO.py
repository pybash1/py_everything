import os
import shutil

def readFile(filename):
    file_data = open(filename, 'r').read()
    return file_data

def writeFile(filename, writeData=''): # TODO: Make writeData a positional parameter.
    with open(filename, 'r+') as file:
        file.truncate(0)
        file.write(writeData)
        file.close()
        return True

def clearFile(filename):
    with open(filename, 'r+') as file:
        file.truncate(0)
        return True

def mkDir(dir_name, path):
    if os.mkdir(os.path.join(path, dir_name)):
        return True

def mkFile(file_name, path):
    with open(path+'\\'+file_name, 'w') as f: 
        pass
        return True

def delDir(path, dir_name):
    if os.rmdir(os.path.join(path, dir_name)):
        return True

def delDirRec(path, dir_name):
    if shutil.rmtree(os.path.join(path, dir_name)):
        return True

def delFile(path, file_name):
    if os.remove(os.path.join(path, file_name)):
        return True


class FileIOBase:
    def __init__(self, filename):
        self.filename = filename

    def readFile(self, filename):
        file_data = open(filename, 'r').read()
        return file_data

    def writeFile(self, filename, writeData=''):
        with open(filename, 'r+') as file:
            file.truncate(0)
            file.write(writeData)
            file.close()
            return True

    def clearFile(self, filename):
        with open(filename, 'r+') as file:
            file.truncate(0)
            return True

class FileIOAdvanced:
    def __init__(self, filename):
        self.filename = filename

    def readFile(self, filename):
        file_data = open(filename, 'r').read()
        return file_data

    def writeFile(self, filename, writeData=''):
        with open(filename, 'r+') as file:
            file.truncate(0)
            file.write(writeData)
            file.close()
            return True

    def clearFile(self, filename):
        with open(filename, 'r+') as file:
            file.truncate(0)
            return True

    def mkDir(self, dir_name, path):
        if os.mkdir(os.path.join(path, dir_name)):
            return True

    def mkFile(self, file_name, path):
        with open(path+'\\'+file_name, 'w') as f: 
            pass
            return True

    def delDir(self, path, dir_name):
        if os.rmdir(os.path.join(path, dir_name)):
            return True

    def delDirRec(self, path, dir_name):
        if shutil.rmtree(os.path.join(path, dir_name)):
            return True

    def delFile(self, path, file_name):
        if os.remove(os.path.join(path, file_name)):
            return True
