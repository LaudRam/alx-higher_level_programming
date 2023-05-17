#!/usr/bin/python3

def best_score(a_dictionary):

    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    chk = list(a_dictionary.keys())[0]
    big = a_dictionary[chk]

    for i, j in a_dictionary.items():
        if j > big:
            big = j
            chk = i
    return chk
