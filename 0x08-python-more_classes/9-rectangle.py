#!/usr/bin/python3

''' A rectangle module '''


class Rectangle():
    ''' A rectangle class'''
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        ''' Initialises a new rectangle

            Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        '''
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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

    def area(self):
        ''' Returns the rectangle area '''
        return self.height * self.width

    def perimeter(self):
        ''' Returns the rectangle perimeter '''
        if self.width == 0 or self.height == 0:
            return 0

        return (self.height + self.width) * 2

    def __str__(self):
        ''' Prints rectangle using '#' '''
        symbol = str(self.print_symbol)
        rectangle = ''
        if self.width == 0 or self.height == 0:
            return rectangle

        for i in range(1, self.height):
            rectangle += symbol * self.width + '\n'
        rectangle += symbol * self.width
        return rectangle

    def __repr__(self):
        ''' Returns string representation of the rectangle '''
        rep = '{}({}, {})'.format(self.__class__.__name__, self.width,
                                  self.height)
        return rep

    def __del__(self):
        ''' Prints a message when an instance of rectangle is deleted'''
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        ''' Returns the biggest rectangle based on the area

            Args:
                rect_1: first rectangle
                rect_2: second rectangle
            Raises:
                TypeError: if either rect_1 or rect_2 is not a rectangle
        '''
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        ''' Returns a new Rectangle instance with width == height == size '''
        return cls(size, size)
