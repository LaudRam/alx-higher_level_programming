#!/usr/bin/python3

def weight_average(my_list=[]):

    if my_list and len(my_list):
        x = 0
        y = 0

        for tup in my_list:
            x += (tup[0] * tup[1])
            y += (tup[1])
        return (x/y)
    return 0
