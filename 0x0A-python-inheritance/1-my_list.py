#!/usr/bin/python3
''' MyList module '''


class MyList(list):
    ''' A subclass of list '''
    def __init__(self):
        ''' Initialises the object '''
        super().__init__()

    def print_sorted(self):
        ''' Prints sorted list '''
        print(sorted(self))
