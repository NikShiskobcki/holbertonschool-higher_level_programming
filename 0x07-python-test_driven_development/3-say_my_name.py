#!/usr/bin/python3
"""says th name"""


def say_my_name(first_name, last_name=""):
    """says the name"""
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    if (first_name) and (last_name):
        print(f"My name is {first_name} {last_name}")
    else:
        if (first_name) and (not last_name):
            print(f"My name is {first_name} ")
        else:
            if (first_name == "") and (last_name):
                print(f"My name is {last_name}")
    if first_name == "" and last_name == "":
        print(f"My name is    ")
