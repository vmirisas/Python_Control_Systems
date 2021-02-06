import numpy as np
from numpy.polynomial import Polynomial as P

p = P([2, 0, 5, -6])
b = P([-1, 1])
print(p)

# conv(p,q)
conv = p * b
print(conv)  # 1 way
print(f"numpy: {np.convolve(p, b)}")  # 2 way + domain, window
print(f"polymul: {np.polymul(p, b)}")

# [q,r] = deconv(a,b)
P = np.array([2, 0, 5, -6])
B = np.array([-1, 1])
print(f"deconv :{np.polydiv(P, B)}")
# working with arrays
print(f"polymul: {np.polymul(P, B)}")
print(f"numpy: {np.convolve(P, B)}")

# r = roots(p)
rootsP = np.roots(P)
print(f"rootsP :{rootsP}")

# p = polyder(r)
polyP = np.poly(rootsP)
print(polyP)

# polyder(p, m=1)
# m: Order of differentiation (default: 1)
polyderP = np.polyder(P)
print(polyderP)
