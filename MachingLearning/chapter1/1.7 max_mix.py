import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# 最大值
print(np.max(matrix))

# 最小值
print(np.min(matrix))

# 每一列的最大值
print(np.max(matrix,axis=0))  # [7 8 9]

# 每一行的最大值
print(np.max(matrix,axis=1))  # [3 6 9]