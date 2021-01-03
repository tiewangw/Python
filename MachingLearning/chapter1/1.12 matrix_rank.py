import numpy as np

matrix = np.array([
    [1,1,1],
    [1,1,10],
    [1,1,15]
])

# 返回矩阵的秩: 就是由它的列或行展开的向量空间的维度。
print(np.linalg.matrix_rank(matrix))  # 2
