'Метод Гаусса: с выбором главного элемента'
import numpy as np
from fractions import Fraction as Frac


R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix, M, L = np.zeros((R, C), dtype=Frac), [[0 for i in range(R)] for j in range(C)], [[0 for x in range(R)] for y in range(C)]
print("Enter the rows:")

for i in range(R):
    a = np.array(list(map(Frac, input().split())))
    matrix[i] = a

for nrow in range(len(matrix)):
    pivot = nrow + np.argmax(abs(matrix[nrow:, nrow]))
    if pivot != nrow:
        row_copy = np.copy(matrix[nrow])
        matrix[nrow] = matrix[pivot]
        matrix[pivot] = row_copy

for k in range(R - 1):
    for row in range(k + 1, R):
        L[row][k] = matrix[row][k] / matrix[k][k]
        for column in range(C - 1):
            matrix[row][column] = matrix[row][column] - L[row][k] * matrix[k][column]
        matrix[row][C - 1] = matrix[row][C - 1] - L[row][k] * matrix[k][C - 1]
matrix[R - 1][C - 1] /= matrix[R - 1][R - 1]

for i in range(R - 2, -1, -1):
    for j in range(i + 1, R):
        matrix[i][C - 1] -= matrix[i][j] * matrix[j][C - 1]
    matrix[i][C - 1] /= matrix[i][i]

for i in range(1, R + 1):
    print('x[', i, '] = ', matrix[i - 1][C - 1], sep='')
