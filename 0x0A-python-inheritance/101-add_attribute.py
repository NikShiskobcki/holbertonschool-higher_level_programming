#!/usr/bin/python3
"""function"""


def add_attribute(mc, name, other):
    """adds attribute"""
    if hasattr(mc, '__dict__'):
        setattr(mc, name, other)
    else:
        raise TypeError("can't add new attribute")
