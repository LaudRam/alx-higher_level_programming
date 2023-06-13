#!/usr/bin/python3
''' Module for load_from_json_file function '''
import json


def load_from_json_file(filename):
    ''' Creates an Object from a JSON file '''
    with open(filename, 'r') as j_file:
        my_obj = json.load(j_file)
        return my_obj
