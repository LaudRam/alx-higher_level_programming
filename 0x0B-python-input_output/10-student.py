#!/usr/bin/python3
''' Module for class Student '''


class Student():
    ''' Defines a student '''
    def __init__(self, first_name, last_name, age):
        ''' Initialises Student

            Args:
            first_name (str): name of student
            last_name (str): surname of student
            age (int): age of student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None):
        ''' Retrieves disctionary representation of Student
            Args:
            attr (list): attribute names
        '''
        if attr is not None:
            result = {j: self.__dict__[j] for j in self.__dict__.keys() & attr}
            return result
        else:
            return self.__dict__
