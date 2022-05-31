#!/usr/bin/python3
"""function"""
from sys import *


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"
try:
    lst = load_from_json_file(filename)
except FileNotFoundError:
    lst = []

r = lst + argv[1:]
save_to_json_file(r, filename)
