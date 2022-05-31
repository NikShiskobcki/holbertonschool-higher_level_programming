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
                if i in self.__dict__:
                    res[i] = self.__dict__[i]
            return res
        else:
            return self.__dict_

    def reload_from_json(self, json):
        """replaces all attributes of student"""
        if json:
            self.__dict__ = json
