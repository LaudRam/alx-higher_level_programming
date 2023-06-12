#!/usr/bin/python3
''' MyInt class module '''


class MyInt(int):
    ''' Inverts int operators == and != '''
    def __init__(self, num):
        self.num = num

    def _eq_(self, value):
        ''' Overide == with != behavior '''
        return self.num != value

    def _ne_(self, value):
        ''' Overide != with == behavior '''
        return self.num == value

    def __str__(self):
        return str(self.num)
