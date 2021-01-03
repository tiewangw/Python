import numpy as np

matrix = np.array([
    [1,2,3],
    [2,4,6],
    [7,8,9]
])

# 使用det 计算矩阵的行列式
print(np.linalg.det(matrix))