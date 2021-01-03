import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# 计算特征值和特征向量
eigenvalues, eignvectors = np.linalg.eig(matrix)

# 查看特征值
print(eigenvalues)
# [ 1.61168440e+01 -1.11684397e+00 -9.75918483e-16]


#  查看特征向量
print(eignvectors)
# [[-0.23197069 -0.78583024  0.40824829]
#  [-0.52532209 -0.08675134 -0.81649658]
#  [-0.8186735   0.61232756  0.40824829]]

