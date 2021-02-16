def read_file(filename):
    file_data = open(filename, 'r').read()
    return file_data

def write_file(filename, writeData=''):
    with open(filename, 'r+') as file:
        file.truncate(0)
        file.write(writeData)
        file.close()
