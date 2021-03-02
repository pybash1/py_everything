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
