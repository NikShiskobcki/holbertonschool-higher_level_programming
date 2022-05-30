#!/usr/bin/python3
"""function"""


class MyInt(int):
    """rebel class"""

    def __eq__(self, other):
        """change to false"""
        return False

    def __ne__(self, other):
        """change to true"""
        return True
