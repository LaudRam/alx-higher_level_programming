#!/usr/bin/python3

''' Matrix multiplying using module NumPy '''
import numpy


def lazy_matrix_mul(m_a, m_b):
    ''' Multiplies 2 matrices

        Args:
            m_a (list): first matrix
            m_b (list): second matrix
    '''
    return numpy.matmul(m_a, m_b)