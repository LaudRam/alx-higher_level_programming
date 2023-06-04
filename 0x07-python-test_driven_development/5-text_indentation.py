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

    lett = 0
    while lett < len(text) and text[lett]:
        lett += 1

    while lett < len(text):
        print(text[lett], end='')
        if text[lett] == '\n' or text[lett] in '.?:':
            if text[lett] in '.?:':
                print('\n')
            lett += 1
            while lett < len(text) and text[lett] == ' ':
                lett += 1
            continue
        lett += 1
