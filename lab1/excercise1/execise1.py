import numpy as np
from numpy.linalg import inv, det
np.seterr(all='ignore')# for division by zero (optional)


A = np.array([[3, -7, 5], [1, 0, 0], [8, 3, 1]])
B = np.array([[4, 7, 6], [0, -4, 1], [5, -8, 3]])

print(f"Πινακας A: \n{A}")
print(f"Πινακας Β: \n{B}")

#A
sumAB = np.add(A, B)
subAB = np.subtract(A, B)

multiAB = np.multiply(A, B)
productAB = np.dot(A, B)

divisionAB1 = np.divide(A, B)
divisionAB2 = A / B

print(f"sumAB: \n{sumAB}")
print(f"subAB: \n{subAB}")
print(f"multiAB: \n{multiAB}")
print(f"productAB: \n{productAB}")
print(f" divisionAB1: \n{divisionAB1}")
print(f" divisionAB2: \n{divisionAB2}")

#B
C1 = np.dot(A, inv(B))
print(C1)

C2 = np.dot(inv(A), B)
print(C2)

C3a = np.dot(B,A)
C3 = np.dot(det(inv(A)), C3a)
print(C3)

C4a = np.dot(inv(B), A)
C4 = np.dot(det(B), C4a)
print(C4)