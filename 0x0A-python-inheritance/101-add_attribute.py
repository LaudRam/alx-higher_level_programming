#!/usr/bin/python3
''' Module for adding attributes '''


def add_attribute(obj, name, value):
    ''' Adds attribute to object where possible '''
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
