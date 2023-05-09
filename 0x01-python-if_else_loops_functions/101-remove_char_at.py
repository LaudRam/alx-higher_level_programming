#!/usr/bin/python3

def remove_char_at(str, n):

    i = str[: n]        # store characters before nth position
    j = str[n + 1:]     # store characters after nth position
    return (i + j)
