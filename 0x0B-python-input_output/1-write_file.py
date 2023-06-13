#!/usr/bin/python3
''' Module for write_file function '''


def write_file(filename="", text=""):
    ''' Writes a string to a text file
        and returns the number of characters

        Args:
            text (str): text to be written
    '''
    with open(filename, mode='w', encoding='UTF-8') as f:
        return f.write(text)
