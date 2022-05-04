#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_mtx = matrix.copy()

    for i in range(len(matrix)):
        new_mtx[i] = list(map(lambda x: x*x, matrix[i]))
    return(new_mtx)
