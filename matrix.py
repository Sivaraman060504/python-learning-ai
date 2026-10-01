import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

print(matrix[0,2])
print(matrix[1,1])
print(matrix[1])
print(matrix[:,0])

print("Arrays:",matrix)
print("dimension", matrix.ndim)
print("shape", matrix.shape)
print("size", matrix.size)
print("type",matrix.dtype)

print("Avarage",matrix.mean())
print("total count",matrix.sum())
print("min number",matrix.min())
print("max number",matrix.max())

print("column totals",matrix.sum(axis=0))
print("rows totals",matrix.sum(axis=1))