#!/usr/bin/python3

''' A rectangle module '''


class Rectangle():
    ''' A rectangle class'''
    def __init__(self, width=0, height=0):
        ''' Initialises a new rectangle

            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' Retrieves rectangle width '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' Sets the width of the rectangle

            Raises:
                TypeError: if width is not an integer
                ValueError: if width < 0
        '''
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        ''' Retrieves rectangle height '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' Sets the height of the rectangle

            Raises:
                TypeError: if height is not an integer
                ValueError: if height < 0
        '''
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
