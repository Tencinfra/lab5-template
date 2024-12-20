#!/usr/bin/env python3
#ctenzin

def read_file_string(file_name):
    #take file_name as string for a file name, returns its entire contents as a string
    with open(file_name, 'r') as file:
        return file.read()

def read_file_list(file_name):
    # takes a file_name as string for  file name,
    # returns its entire contents as a lsit of lines without new-line characters
    with open (file_name, 'r') as file:
        return [line.strip('\n') for line in file]


if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))



