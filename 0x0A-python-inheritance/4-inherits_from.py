#!/usr/bin/python3
"""function"""


def inherits_from(obj, a_class):
    """inherits"""
    if type(obj) != a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
