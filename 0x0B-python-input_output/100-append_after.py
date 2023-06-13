#!/usr/bin/python3
''' Module for append_after function '''


def append_after(filename="", search_string="", new_string=""):
    ''' Appends text after finding key string '''
    my_str = ''

    with open(filename, encoding='UTF-8') as fd:
        for line in fd:
            my_str += line
            if search_string in line:
                my_str += new_string

    with open(filename, mode='w') as fd:
        fd.write(my_str)
