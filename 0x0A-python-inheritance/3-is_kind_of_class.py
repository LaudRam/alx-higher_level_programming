#!/usr/bin/python3
''' Module for is_kind_of_class function '''


def is_kind_of_class(obj, a_class):
    ''' Checks if object is an instance or inherited instance of a class'''
    if isinstance(obj, a_class):
        return True
    return False
