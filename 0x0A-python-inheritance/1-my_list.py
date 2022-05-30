#!/usr/bin/python3
"""my list class"""


class MyList(list):
    """class myList"""

    def print_sorted(self):
        """prints sorted list"""
        print(sorted(self))
