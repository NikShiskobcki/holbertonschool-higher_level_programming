#!/usr/bin/python3
def weight_average(my_list=[]):
    if my_list == []:
        return 0
    up = 0
    low = 0
    for i in my_list:
        up = up + (i[0] * i[1])
        low = low + i[1]
    prom = up / low
    return prom
