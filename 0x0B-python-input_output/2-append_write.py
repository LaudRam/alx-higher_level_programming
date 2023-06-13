#!/usr/bin/python3
''' Module for append_write function '''


def append_write(filename="", text=""):
    ''' Appends a string at the end of a text file
        and returns number of characters added
    '''
    with open(filename, 'a', encoding='UTF-8') as a_file:
        return a_file.write(text)
