#!/usr/bin/python3
"""function"""


def append_write(filename="", text=""):
    """appends text and returns number of chars"""
    with open(filename, 'a', encoding="utf-8") as f:
        a = f.write(text)
    return a
