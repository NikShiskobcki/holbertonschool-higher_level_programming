#!/usr/bin/python3
"""prints square"""


def print_square(size):
    """prints a square"""
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    if size == 0:
        return
    else:
        for i in range(size):
            for i in range(size):
                print("#", end="")
            print("")
