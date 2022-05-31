#!/usr/bin/python3
"""function"""
import json


def save_to_json_file(my_obj, filename):
    """writes an object to txt file using json"""
    with open(filename, 'w', encoding="utf-8") as f:
        x = json.dumps(my_obj)
        f.write(x)
