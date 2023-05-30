#!/usr/bin/python3

''' Square module '''


class Square():
    ''' Defines a square '''

    def __init__(self, size=0, position=(0, 0)):
        ''' Initialisation of instance attributes

            Args:
                size (int): size of square, non-negative
                position (int, tuple): position of square
        '''
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        ''' Retrieves square position '''
        return self.__position

    @position.setter
    def position(self, value):
        ''' Updating private attributes

            Args - value (int): position value to set

            Raises:
                TypeError: if position is not a tuple of 2 positive integers
        '''
        if isinstance(value, tuple) and len(value) == 2:
            if isinstance(value[0], int) and isinstance(value[1], int):
                if value[0] >= 0 and value[1] >= 0:
                    self.__position = value
                    return
        raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        ''' Prints the square in # characters '''
        if self.__size == 0:
            return ("")

        for i in range(self.__position[1]):
            print()

        for j in range(self.__size - 1):
            print('{}{}'.format(' ' * self.__position[0], '#' * self.__size))
        return ('{}{}'.format(' ' * self.__position[0], '#' * self.__size))

    def __str__(self):
        return self.my_print()
