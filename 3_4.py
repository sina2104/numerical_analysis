'Метод прогонки'
import numpy as np
from fractions import Fraction as Frac


R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix, P, Q, X = [], [0] * R, [0] * R, [0] * R
print("Enter the rows:")

for i in range(R):
    a = list(map(Frac, input().split()))
    matrix.append(a)

alpha = list(np.diag(matrix, k=-1))
betta = list(-1 * np.diag(matrix))
gamma = list(np.diag(matrix, k=1))
delta = list(np.array(matrix)[:, R])

P[0] = gamma[0] / betta[0]
Q[0] = delta[0] / -betta[0]

for i in range(1, R - 1):
    P[i] = gamma[i] / (betta[i] - alpha[i - 1] * P[i-1])
    Q[i] = (alpha[i - 1] * Q[i-1] - delta[i]) / (betta[i] - alpha[i - 1] * P[i - 1])

X[R-1] = (alpha[2] * Q[2] - delta[3]) / (betta[3] - alpha[2] * P[2])
for i in range(R - 2, -1, -1):
    X[i] = P[i] * X[i + 1] + Q[i]

for i in range(1, R + 1):
    print('x[', i, '] = ', X[i - 1], sep='')
