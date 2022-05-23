#!/usr/bin/python3
"""divides amtrix"""


def matrix_divided(matrix, div):
    """divides matrix"""
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    """checks for empty row or not int or float elements"""
    for row in matrix:
        if len(row) == 0:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        for x in row:
            if type(x) is not int and type(x) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    """checks for length of rows"""
    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
    

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = []
    for i in matrix:
        new.append(list(map(lambda x: round(x/div, 2), i)))
    return new


