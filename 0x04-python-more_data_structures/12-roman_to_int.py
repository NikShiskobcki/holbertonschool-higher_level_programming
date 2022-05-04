#!/usr/bin/python3
def conv(i):
    if i == "M":
        return 1000
    if i == "D":
        return 500
    if i == "C":
        return 100
    if i == "L":
        return 50
    if i == "X":
        return 10
    if i == "V":
        return 5
    if i == "I":
        return 1


def roman_to_int(roman_string):
    if roman_string == None:
        return 0

    res = 0
    for i in range(len(roman_string)):
        value = conv(roman_string[i])
        if len(roman_string) > i+1:
            if value < conv(roman_string[i+1]):
                res = res - value
            else:
                res = res + value
        else:
            res = res + value
    return res
