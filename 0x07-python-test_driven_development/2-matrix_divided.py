#!/usr/bin/python3

''' Module for diving elements '''


def matrix_divided(matrix, div):
    ''' Divides all elements of a matrix

        Args:
            matrix (list): list of integers or floats
            div (int/float): divisor

        Raise:
            TypeError: if matrix is not a list of lists of integers/floats
            TypeError: if matrix contains rows of different sizes
            TypeError: if div is not an integer or float
            ZeroDivisionError: if div is 0

        Return: new matrix
    '''
    new_matrix = []
    try:
        length = len(matrix[0])
    except (TypeError):
        pass

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    msg = 'matrix must be a matrix (list of lists) of integers/floats'

    for row in matrix:
        new_row = []

        if length != len(row):
            raise TypeError('Each row of the matrix must have the same size')
        if not isinstance(row, list):
            raise TypeError(msg)
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError(msg)
            res = round(i / div, 2)
            new_row.append(res)
        new_matrix.append(new_row)
    return new_matrix
