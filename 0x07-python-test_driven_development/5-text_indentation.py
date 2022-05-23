#!/usr/bin/python3
"""indents text"""

def text_indentation(text):
    """indents text"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    i = 0
    while (i < len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print(text[i], end="")
            print('\n')
            i += 1
            while (text[i] == ' '):
                i += 1
        else:
            print(text[i], end="")
            i += 1
