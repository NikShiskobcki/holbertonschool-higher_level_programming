#!/usr/bin/python3
"""function"""


class Student:
    """class student"""

    def __init__(self, first_name, last_name, age):
        """init"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dict representation"""
        if type(attrs) is list:
            res = {}
            for i in attrs:
                if i in self.__dict:
                    res[i] = self.dict[i]
        else:
            return dict(self.__dict__)
