import numpy as np

p = np.array([3, 0, 5, -1, -8])
q = np.array([2, -1, 3])

# A
print(np.roots(p))
print(np.roots(q))

print(np.polyder(p))
print(np.polyder(q))

# B
sumpq = np.polyadd(p, q)
prodpq = np.polymul(p, q)

print(np.roots(sumpq))
print(np.polyder(sumpq))
print(np.roots(prodpq))
print(np.polyder(prodpq))
