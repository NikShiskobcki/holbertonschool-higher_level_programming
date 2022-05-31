#!/usr/bin/python3
"""function"""


def read_file(filename=""):
    """reads file"""
    with open(filename, 'r', encoding="utf-8") as f:
        r = f.read()
    print(r)
