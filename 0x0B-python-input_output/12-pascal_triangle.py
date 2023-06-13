#!/usr/bin/python3
''' Module for pascal_triangle function '''


def pascal_triangle(n):
    """ Returns a list of lists of integers
        representing the Pascal’s triangle
    """
    rows = [[1 for x in range(y + 1)] for y in range(n)]

    for n in range(n):
        for y in range(n - 1):
            rows[n][y + 1] = sum(rows[n - 1][y:y + 2])
    return rows
