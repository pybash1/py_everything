import os
import shutil

def read_file(filename):
    file_data = open(filename, 'r').read()
    return file_data

def write_file(filename, writeData=''):
    with open(filename, 'r+') as file:
        file.truncate(0)
        file.write(writeData)
        file.close()
        return True

def clear_file(filename):
    with open(filename, 'r+') as file:
        file.truncate(0)
        return True

def mk_dir(dir_name, path):
    if os.mkdir(os.path.join(path, dir_name)):
        return True

def mk_file(file_name, path):
    with open(path+file_name, 'w') as f: 
        pass
        return True

def del_dir(path, dir_name):
    if os.rmdir(os.path.join(path, dir_name)):
        return True

def del_dir_rec(path, dir_name):
    if shutil.rmtree(os.path.join(path+dir_name)):
        return True

def del_file(path, file_name):
    if os.remove(os.path.join(path+file_name)):
        return True


class FileIOBase:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self, filename):
        file_data = open(filename, 'r').read()
        return file_data

    def write_file(self, filename, writeData=''):
        with open(filename, 'r+') as file:
            file.truncate(0)
            file.write(writeData)
            file.close()
            return True

    def clear_file(self, filename):
        with open(filename, 'r+') as file:
            file.truncate(0)
            return True

class FileIOAdvanced:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self, filename):
        file_data = open(filename, 'r').read()
        return file_data

    def write_file(self, filename, writeData=''):
        with open(filename, 'r+') as file:
            file.truncate(0)
            file.write(writeData)
            file.close()
            return True

    def clear_file(self, filename):
        with open(filename, 'r+') as file:
            file.truncate(0)
            return True

    def mk_dir(self, dir_name, path):
        if os.mkdir(os.path.join(path, dir_name)):
            return True

    def mk_file(self, file_name, path):
        with open(path+file_name, 'w') as f: 
            pass
        return True

    def del_dir(self, path, dir_name):
        if os.rmdir(os.path.join(path, dir_name)):
            return True

    def del_dir_rec(self, path, dir_name):
        if shutil.rmtree(os.path.join(path+dir_name)):
            return True

    def del_file(self, path, file_name):
        if os.remove(os.path.join(path+file_name)):
            return True
