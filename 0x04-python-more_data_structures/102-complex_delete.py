#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    del_keys = []

    for x in a_dictionary:
        if a_dictionary[x] == value:
            del_keys.append(x)
    for x in del_keys:
        del a_dictionary[x]
    return a_dictionary
