#!/usr/bin/python3
def uniq_add(my_list=[]):
    res = 0
    s = set(my_list)
    my_list = list(s)
    for i in range(len(my_list)):
        res = res + my_list[i]
    return res
