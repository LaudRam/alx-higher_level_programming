#!/usr/bin/python3

''' Module for printing square '''


def print_square(size):
    ''' Prints a square with # characters

        Args:
            size (int): length of the square
        Raises:
            TypeError: if size is not an integer
            ValueError: if size < 0
    '''
    square = ''
    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    for i in range(size):
        square += '#' * size + '\n'
    print(square, end='')
