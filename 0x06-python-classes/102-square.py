#!/usr/bin/python3

''' Square module '''


class Square():
    ''' Defines a square '''

    def __init__(self, size=0):
        ''' Initialisation of instance attributes

            Args - size (int): size of square, non-negative

            Raises:
                TypeError: if size is not an integer
                ValueError: if size < 0
        '''
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        ''' Calculates area of square

            Return: current square area
        '''
        return self.__size ** 2

    @property
    def size(self):
        ''' Retrieves size of square '''

        return self.__size

    @size.setter
    def size(self, value):
        ''' Updating private attributes

            Args - value (int): non-negative

            Raises:
                TypeError: if size is not an integer
                ValueError: if size < 0
        '''
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def __eq__(self, other):
        ''' Defines the == comparison to a square area '''
        return (self.area() == other.area())

    def __ne__(self, other):
        ''' Defines the != comparison to a square area '''
        return (self.area() != other.area())

    def __gt__(self, other):
        ''' Defines the > comparison to a square area '''
        return (self.area() > other.area())

    def __ge__(self, other):
        ''' Defines the >= comparison to a square area '''
        return (self.area() >= other.area())

    def __lt__(self, other):
        ''' Defines the < comparison to a square area '''
        return (self.area() < other.area())

    def __le__(self, other):
        ''' Defines the <= comparison to a square area '''
        return (self.area() <= other.area())
