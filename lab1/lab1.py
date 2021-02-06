import numpy as np
from numpy import random

M = 10
print(M)

array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# ATTRIBUTES OF AN ARRAY/MATRIX
print("attributes of an array")
print(f"the array is:\n {array}")
print(f"the length of the array is: {len(array)}")
print(f"Tuple of array dimensions: {array.shape}")
print(f"Number of array dimensions: {array.ndim}")
print(f"Number of elements in the array: {array.size}")
print(f"Length of one array element in bytes: {array.itemsize}")
print("")

# INDEXING AND SLICING ARRAYS/MATRICES
print(f"a[0,1] = {array[0, 1]}")  # returns the element of the array in the possition (row:0, column:1)
print(f"a[1:3] = \n{array[1:3]}")  # returns all the elements from row:1 - row:2 (without row:3)
print(f"a[0:2,0] = {array[0:2, 0]}")  # show the elements of from rows:[0,2) and column:[0] of the array
print(f"a[0:2,1] = {array[0:2, 1]}")  # show the elements of from rows:[0,2) and column:[1] of the array
array[0,1]=123
print(f"a[0,1]= {array[0,1]}")  # show the elements of from rows:[0,2) and column:[1] of the array

# ARRAY/MATRIX CREATING TOOLS
"""numpy.arange([start, ]stop, [step, ]dtype=None, *, like=None)"""
# start: Start of interval. The interval includes this value. The default start value is 0.
# stop:  End of interval. The interval does not include this value, except in some cases where step is not an integer and floating point round-off affects the length of out.
# dtype: The type of the output array. If dtype is not given, infer the data type from the other input arguments.
# like: Reference object to allow the creation of arrays which are not NumPy arrays
# returns arange : ndarray

a1 = np.arange(3,7)
a2 = np.arange(1,5)
a = np.append(a1, a2)  # Append values to the end of an array
print(a)

# array2 = np.append(np.arange(3, 7), np.arange(1, 5)).reshape(2, 4)
b1 = np.arange(1, 5)  # [1, 2, 3, 4]
b2 = np.arange(3, 7)  # [3, 4, 5, 6]
b = np.vstack((b2, b1))  # stack arrays in sequence vertically
print(b)

print(f"b row[1] = {b[1, :]}")  # returns all the elements of the row:1
print(f"b column[2] = {b[:, 2]}")  # returns all the elements of the column:2

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)
# start: The starting value of the sequence.
# stop: The end value of the sequence, unless endpoint is set to False. In that case, the sequence consists of all but the last of num + 1 evenly spaced samples, so that stop is excluded. Note that the step size changes when endpoint is False.
# num: Number of samples to generate. Default is 50. Must be non-negative.
# endpoint: If True, stop is the last sample. Otherwise, it is not included. Default is True.
# retstep : If True, return (samples, step), where step is the spacing between samples.
# dtype: The type of the output array. If dtype is not given, the data type is inferred from start and stop. The inferred dtype will never be an integer; float is chosen even if the arguments would produce an array of integers.
# axis: The axis in the result to store the samples. Relevant only if start or stop are array-like. By default (0), the samples will be along a new axis inserted at the beginning. Use -1 to get an axis at the end.
print(f"linespace{np.linspace(2.0, 3.0, num=5)}")
print(f"linespace{np.linspace(2.0, 3.0, num=5, endpoint=False)}")
print(f"linespace{np.linspace(2.0, 3.0, num=5, retstep=True)}")


# SPECIAL CASES
# random elements
# random([size, dtype, out])

rng = np.random.default_rng(12345)

rng1 = rng.random((2, 4))
print(rng1)


rng2 = rng.random((3, 3))
print(rng2)

rng3 = random.randint(99,100, size=(3, 5))
print(rng3)

# zeros
# zeros(shape[, dtype, order, like])
zeros1 = np.zeros((2, 4), int)
zeros2 = np.zeros((3, 3))
print(zeros1)
print(zeros2)

# ones
# ones(shape[, dtype, order, like])
ones1 = np.ones((2, 4), int)
ones2 = np.ones((3, 3))
print(ones1)
print(ones2)


# LINEAR SPACES
# linspace(start, stop, num).astype(int)
# start: The starting value of the sequence
""" stop: The end value of the sequence, unless endpoint is set to False. 
In that case, the sequence consists of all but the last of num + 1 evenly spaced samples, so that stop is excluded. 
Note that the step size changes when endpoint is False."""
# num: Number of samples to generate. Default is 50. Must be non-negative.

ln1 = np.linspace(3, 9, 7)
print(ln1)

ln2 = np.linspace(53, 80, 10)
ln3 = np.arange(53, 81, 3)
print(ln2)
print(ln3)

