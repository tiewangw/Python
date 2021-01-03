import numpy as np

matrix_a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

matrix_b = np.array([
    [1,2,3],
    [0,2,6],
    [7,9,9]
])

# 将两个矩阵相加
print(np.add(matrix_a,matrix_b))
print(matrix_a+matrix_b)

print("-------------------------")

# 将两个矩阵相减
print(np.subtract(matrix_a,matrix_b))
print(matrix_a-matrix_b)