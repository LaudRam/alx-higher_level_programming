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

    def to_json(self, attrs=None):
        ''' Retrieves dictionary representation of Student
            Args:
            attr (list): attribute names
        '''
        if type(attrs) is list and all([type(x) == str for x in attrs]):
            result = {j: v for j, v in self.__dict__.items() if j in attrs}
            return result
        else:
            return self.__dict__.copy()

    def reload_from_json(self, json):
        ''' Loads attributes from json '''
        for key, value in json.items():
            self.__dict__[key] = value
