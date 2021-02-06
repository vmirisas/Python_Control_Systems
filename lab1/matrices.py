import numpy as np
from numpy.linalg import matrix_power, inv, det



# Two matrices are initialized by value
x = np.array([[1, 2], [4, 5]])
y = np.array([[7, 8], [9, 10]])
#  add()is used to add matrices
print ("Addition of two matrices: ")
print (np.add(x,y))

# subtract()is used to subtract matrices
print ("Subtraction of two matrices : ")
print (np.subtract(x,y))

# divide()is used to divide matrices
print ("Matrix Division : ")
print (np.divide(x,y))

print ("Multiplication of two matrices: ")
print (np.multiply(x,y))
print ("The product of two matrices : ")
print (np.dot(x,y))
print ("square root is : ")
print (np.sqrt(x))
print ("The summation of elements : ")
print (np.sum(y))
print ("The column wise summation  : ")
print (np.sum(y,axis=0))
print ("The row wise summation: ")
print (np.sum(y,axis=1))
# using "T" to transpose the matrix
print ("Matrix transposition : ")
print (x.T)

#  C = A^3, (needs from numpy.linalg import matrix_power)
print(matrix_power(x, 3))

# C = A.^3 | C = A.^B
print(np.power(x, 3))
print(np.power(x, y))

# A^(-1), inv(A) (needs from numpy.linalg import inv)
print(inv(x))

# det(A) (needs from numpy.linalg import det)
print(det(x))

# abs(A)
ar = np.array([[-1.2, 1.2],[-4.6, -3]])
print(abs(x))

# C = A\B
B = np.array([[2],[4]])
b = np.array([[4],[4]])
x = np.linalg.lstsq(B, b,rcond=None)
print(x)

# amax(A), amin(A), sum(A), prod(A) (along axis=0 or 1)
ar1 = np.array([[1,5,9,6],[5,8,2,8],[7,3,6,4]])
max_horizontal = np.amax(ar1, axis=0)
max_vertical = np.amax(ar1, axis=1)

min_horizontal = np.amin(ar1, axis=0)
min_vertical = np.amin(ar1, axis=1)

sum_horizontal = np.sum(ar1, axis=0)
sum_vertical = np.sum(ar1, axis=1)

prod_horizontal = np.prod(x, axis=0)
prod_vertical = np.prod(ar1, axis=1)

print(f"max_horizontal = {max_horizontal}")
print(f"max_vertical = {max_vertical}")
print(f"min_horizontal = {min_horizontal}")
print(f"min_vertical = {min_vertical}")
print(f"sum_horizontal = {sum_horizontal}")
print(f"sum_vertical = {sum_vertical}")
print(f"prod_horizontal = {prod_horizontal}")
print(f"prod_vertical = {prod_vertical}")


