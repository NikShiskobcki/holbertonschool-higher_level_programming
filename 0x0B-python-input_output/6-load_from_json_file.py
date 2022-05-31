#!/usr/bin/python3
"""function"""
import json


def load_from_json_file(filename):
    """creates an obj from json file"""
    with open(filename, 'r') as f:
        x = json.load(f)
    return x
