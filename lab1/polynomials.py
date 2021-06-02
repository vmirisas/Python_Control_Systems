import numpy as np
from numpy.polynomial import Polynomial as P

poly1 = P([2, -1, 5, -6])
poly2 = P([2, 0, 1, 0])
print(poly1)
print(poly2)

p1 = np.array([2, -1, 5, -6])
p2 = np.array([2, 0, 1, 0])
print(f"polynomial add p1 + p2: {np.polyadd(p1, p2)}")
print(f"polynomial multiply p1 * p2: {np.polymul(p1, p2)}")
print(f"polynomial divide p1 / p2: {np.polydiv(p1, p2)}")

rootsP1 = np.roots(p1)
print(f"roots of p1: {rootsP1}")

poly = np.poly(rootsP1)
print(f"polynomial creation with roots of 'rootsP1': {poly}")

polyD = np.polyder(p1)
print(f"derivative of the polynomial: {polyD}")
