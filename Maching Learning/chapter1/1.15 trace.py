import numpy as np

matrix = np.array([
    [1,2,3],
    [2,4,6],
    [7,8,9]
])

# 返回矩阵的迹； 矩阵的对角线元素之和
print(matrix.trace())

# 也可以先返回矩阵的对角线元素在对齐求和的方式来计算矩阵的迹
print(sum(matrix.diagonal()))
