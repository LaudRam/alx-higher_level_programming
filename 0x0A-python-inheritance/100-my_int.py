#!/usr/bin/python3
''' MyInt class module '''


class MyInt(int):
    ''' Inverts int operators == and != '''
    def _eq_(self, value):
        ''' Overide == with != behavior '''
        return self.real != value

    def _ne_(self, value):
        ''' Overide != with == behavior '''
        return self.real == value
