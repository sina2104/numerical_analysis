"""LU-разложение"""
import numpy as np
from fractions import Fraction as Frac


def show_matrix(mat):
    for i in range(mat.shape[0]):
        for j in range(mat.shape[1]):
            print(mat[i][j], end=' ')
        print("")


R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix, U, L, Y, X = np.zeros((R, C), dtype=Frac), np.diag(np.full(R, Frac(1, 1), dtype=Frac)), \
                  np.zeros((R, R), dtype=Frac), np.zeros(R, dtype=Frac), np.zeros(R, dtype=Frac)
print("Enter the rows:")

for i in range(R):
    matrix[i] = np.array(list(map(Frac, input().split())))

U = matrix[:, :-1]
beta = matrix[:, -1:]
for i in range(R):
    for j in range(i, R):
        L[j][i] = U[j][i] / U[i][i]
for k in range(1, R):
    for i in range(k - 1, R):
        for j in range(i, R):
            L[j][i] = U[j][i] / U[i][i]
    for i in range(k, R):
        for j in range(k - 1, R):
            U[i][j] = U[i][j] - L[i][k - 1] * U[k - 1][j]

print('L =')
show_matrix(L)
print('U =')
show_matrix(U)
print('LU =')
show_matrix(np.dot(L, U))
for i in range(R):
    Y[i] = beta[i]
    for k in range(i):
        Y[i] -= L[i][k] * Y[k]

for i in range(R - 1, -1, -1):
    X[i] = Y[i]
    for k in range(i + 1, R):
        X[i] -= U[i][k] * X[k]
    X[i] /= U[i][i]

for i in range(1, R + 1):
    print('x[', i, '] = ', X[i - 1][0], sep='')
