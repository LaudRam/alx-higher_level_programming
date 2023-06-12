#!/usr/bin/python3
''' Class checking module'''


def is_same_class(obj, a_class):
    ''' Checks if th objects have the same class

        Args:
            obj: object to check
            a_class: class to match obj type to
    '''
    if type(obj) is a_class:
        return True
    return False
