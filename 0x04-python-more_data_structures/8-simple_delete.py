#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    remove_key = a_dictionary.pop(key, None)
    return(a_dictionary)
