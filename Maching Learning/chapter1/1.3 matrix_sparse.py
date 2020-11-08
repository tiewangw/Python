# 稀疏矩阵只保存非零元素并假设剩余元素的值都是0

import numpy as np
from scipy import sparse

#创建一个矩阵
matrix = np.array([
    [0,0],
    [0,1],
    [3,0]
])

# 创建一个压缩的稀疏行（Compressed Sparse Row,CSR） 矩阵
matrix_sparse = sparse.csr_matrix(matrix)

print(matrix_sparse)

# (1, 1)	1
# (2, 0)	3