import sys


def read_file(filename):
    try:
        file = open(filename, mode = 'rt', encoding = 'utf-8')
    except FileNotFoundError:
        return str().join(['Error, file \'', filename, '\' not found!'])
    except:
        return str().join('Unknown error while trying to read file!', filename)
    
    content = file.read()
    file.close()
    
    return content


def write_file(filename, content):
    try:
        file = open(filename, mode = 'wt', encoding = 'utf-8')
    except:
        return str().join(['Cannot open file \'', filename, '\' to write'])

    file.write(content)
    file.close()


FilePathAndName = 'file-read-write-input.txt'
print('Let\'s read content of ', FilePathAndName, '...')
FileContent = read_file(FilePathAndName)
print('Here\'s the content of the file:\n', FileContent)


FilePathAndName = 'file-read-write-output.txt'
OutputFileContent = str ('Output file content')
print('Let\'s write \'', OutputFileContent, '\' to ', FilePathAndName)
write_file(FilePathAndName, OutputFileContent)


print('Now let\'s read content of ', FilePathAndName, '...')
FileContent = read_file(FilePathAndName)
print('Here\'s the content of the file:\n', FileContent)


if OutputFileContent == FileContent:
    print('Hurrah! The file content of ', FilePathAndName, ' equals what we wrote!')
else:
    print('Something went wrong and the content of ', FilePathAndName, ' differs from what we wrote!')
    raise Exception('Something screwy is going on here...') 
