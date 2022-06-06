#!/usr/bin/python3
"""base model"""
import json


class Base():
    """base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns json string representation"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """saves to json file"""
        lst = []
        if list_objs is None:
            list_objs = []
        for j in list_objs:
            lst.append(cls.to_dictionary(j))
        txt = cls.to_json_string(lst)

        filename = ("{}.json".format(cls.__name__))
        with open(filename, 'w') as f:
            f.write(txt)

    @staticmethod
    def from_json_string(json_string):
        """from json to string"""
        lst = []
        if json_string is None or json_string == "":
            return lst
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns instance with attributes set"""
        if cls.__name__ == "Rectangle":
            ins = cls(1, 1)
        elif cls.__name__ == "Square":
            ins = cls(2)
        ins.update(**dictionary)
        return ins

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, 'r') as f:
                data = f.read()
        except FileNotFoundError:
            return []
        aux = []
        lst = cls.from_json_string(data)
        for j in lst:
            aux.append(cls.create(**j))
        return aux
