#!/usr/bin/python3

''' Printing module '''


def text_indentation(text):
    ''' Prints text with 2 new lines after each of these characters:
        '.', '?' and ':'

        Args:
            text (str): text to print

        Raise:
            TypeError: if text is not a string
    '''
    if not isinstance(text, str):
        raise TypeError('text must be a string')

    buff = ''
    for c in text:
        buff += c
        if c == '.' or c == '?' or c == ':':
            while buff[0] == ' ':
                buff = buff[1:]
            print(buff)
            print()
            buff = ''
    if len(buff) != 0:
        try:
            while buff[0] == ' ':
                buff = buff[1:]
        except (ValueError):
            pass
        print(buff, end='')
