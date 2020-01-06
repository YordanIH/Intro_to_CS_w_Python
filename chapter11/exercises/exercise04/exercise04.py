from typing import TextIO,Set
from io import StringIO

def author_names(files_names: list) ->set:
    names=set()
    for file in files_names:
        with open(file, 'r') as read_file:
            lines=read_file.readlines()
            for line in lines:
                list_of_contents=line.split()
                if list_of_contents:
                    if list_of_contents[0].upper()== 'AUTHOR':
                        names.add(list_of_contents[1])
        read_file.close()
    return names
    

if __name__ == '__main__':
    files_names=['authors1','authors2']
    print(author_names(files_names))