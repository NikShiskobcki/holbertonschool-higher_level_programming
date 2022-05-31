#!/usr/bin/python3
"""function"""


def write_file(filename="", text=""):
    """returns number of chars"""
    with open(filename, 'w', encoding="utf-8") as f:
        w = f.write(text)
    return w
