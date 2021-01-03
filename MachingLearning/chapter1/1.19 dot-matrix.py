import numpy as np

matrix_a = np.array([
    [1,1],
    [1,2],
])

matrix_b = np.array([
    [1,3],
    [1,2],
])

# 2个矩阵相乘 方法1
print(np.dot(matrix_a,matrix_b))

print("--------------------")
# 2个矩阵相乘 方法2
print(matrix_a @ matrix_b)

print("--------------------")
# 将2个矩阵对应的元素相乘 ，使用*
print(matrix_a * matrix_b)


