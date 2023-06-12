#!/usr/bin/python3
''' BaseGeometry module '''


class BaseGeometry():
    ''' Class based on 6-base_geometry.py '''
    def area(self):
        ''' Raises exception when called '''
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        ''' Validates that value is a positive integer

            Args:
                name (str): name of parameter
                value (int): parameter to validate
        '''
        if type(value) != int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
