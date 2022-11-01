"""Метод Зейделя"""
import numpy as np
from fractions import Fraction as Frac


R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix, beta, alpha = np.zeros((R, C), dtype=Frac), [[0] for j in range(R)], np.zeros((R, C - 1), dtype=Frac)
print("Enter the rows:")

for i in range(R):
    a = np.array(list(map(Frac, input().split())))
    matrix[i] = a

eps = Frac(input("Enter how precise you want the answer:"))
for nrow in range(len(matrix)):
    pivot = nrow + np.argmax(abs(matrix[nrow:, nrow]))
    if pivot != nrow:
        row_copy = np.copy(matrix[nrow])
        matrix[nrow] = matrix[pivot]
        matrix[pivot] = row_copy
    matrix[nrow] /= matrix[nrow][nrow]

beta = matrix[:, -1:]
for nrow in range(len(matrix)):
    alpha[nrow] = -matrix[nrow, :-1]
    alpha[nrow][nrow] = 0

X1 = beta
time = 0
while True:
    X2 = np.zeros(R, dtype=Frac)
    for i in range(R):
        for j in range(R):
            X2[i] += alpha[i][j] * (X2[j] if j < i else X1[j])
        X2[i] += beta[i]
    time += 1
    if np.amax(abs(X2 - X1)) < eps:
        break
    X1 = X2

for i in range(1, R + 1):
    print('x[', i, '] = ', X2[i - 1][0], sep='')
print("Amount of operations needed:", time)
