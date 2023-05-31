#!/usr/bin/python3

''' Python bytecode '''

import math


class MagicClass():
    '''Defines class that does exactly the same as provided python bytecode'''

    def __init__(self, radius=0):
        ''' Initialises MagicClass

            Args - radius: radius of circle

            Raise - TypeError: if radius is not a number
        '''
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

        def area(self):
            ''' Returns area of the circle '''
            return (math.pi * (self.__radius ** 2))

        def circumference(self):
            ''' Returns circumference of circle '''
            return (2 * math.pi * self.__radius)
