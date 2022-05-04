#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    aux = a_dictionary.copy()
    for key in aux:
        aux[key] *= 2
    return aux
