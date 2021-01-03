import numpy as np

matrix = np.array([
    [1,2,3],
    [2,4,6],
    [7,8,9]
])

# diagonal ：获取矩阵的对角线元素
print(matrix.diagonal())

# offset 在主对角线的上下偏移，获取偏移后的对角线方向的元素

# 返回主对角线向上偏移量为1的对角线元素
print(matrix.diagonal(offset=1))

# 返回主对角线向下偏移量为1的对角线元素
print(matrix.diagonal(offset=-1))