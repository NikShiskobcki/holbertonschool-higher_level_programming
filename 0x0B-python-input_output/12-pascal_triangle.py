#!/usr/bin/python3
"""function"""


def pascal_triangle(n):
    """pascal triangle"""
    lst = []
    lstAux = []
    if n <= 0:
        return []
    for x in range(n):
        lst = [1]
        if x > 0:
            for i in range(x):
                lst.append(sum(lstAux[-1][i:i+2]))
        lstAux.append(lst)
    return (lstAux)
