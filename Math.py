from re import M, T
from collections import namedtuple
from unicodedata import decimal
import numpy as np

V4 = namedtuple('Point4', ['x', 'y', 'z', 'w'])

def multiply_matrix(matrix1, matrix2):
    matrix = [
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
        [0,0,0,0],
    ]
    for i in range(4):
        for j in range(4):
            for k in range(4):
                matrix[i][j] += np.float64(matrix1[i][k] * matrix2[k][j])
            
    return matrix


def multiply_matrix_vector(matrix, vector):
    result = [0,0,0,0]
    for i in range(4):
        for j in range(4):
            result[i] += matrix[i][j] * vector[j]
    return result
