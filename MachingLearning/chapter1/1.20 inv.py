import numpy as np

matrix = np.array([
    [1,4],
    [2,5]
])

# 计算一个矩阵的逆
inv = np.linalg.inv(matrix)
print(inv)
# [[-1.66666667  1.33333333]
#  [ 0.66666667 -0.33333333]]
print("--------------------")

print(matrix @ inv)
# [[1. 0.]
#  [0. 1.]]

