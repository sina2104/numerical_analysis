'Метод Гаусса: метод единственного дления'
import numpy as np
from fractions import Fraction as Frac


R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix, M = [], [[0 for i in range(R)] for j in range(C)]
print("Enter the rows:")

for i in range(R):
    a = np.array(list(map(Frac, input().split())))
    matrix.append(a)

for nrow, row in enumerate(matrix):
    divider = row[nrow]
    row /= divider
    for row_below in matrix[nrow + 1:]:
        factor = row_below[nrow]
        row_below -= factor * row

for nrow in range(len(matrix) - 1, 0, -1):
    row = matrix[nrow]
    for row_above in matrix[:nrow]:
        row_above[-1] -= row_above[nrow] * row[-1]

for i in range(1, R + 1):
    print('x[', i, '] = ', matrix[i - 1][C - 1], sep='')
