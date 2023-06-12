#!/usr/bin/python3
''' Rectangle subclass Square '''


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


class Rectangle(BaseGeometry):
    ''' Defines rectangle using BaseGeometry '''
    def __init__(self, width, height):
        ''' Initialises new rectangle

            Args:
                width (int): width of rectangle
                height (int): height of rectangle
        '''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height

    def area(self):
        ''' Returns area of rectangle '''
        return self.__width * self.__height

    def __str__(self):
        ''' String representation of rectangle '''
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)


class Square(Rectangle):
    ''' Square class '''
    def __init__(self, size):
        ''' Initialises a new square

            Args:
                size (int): size of square
        '''
        self.integer_validator('size', size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)
