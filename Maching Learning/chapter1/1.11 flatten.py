import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# flatten : 将矩阵转换成一个一维数组
print(matrix.flatten())

# flatten 是将矩阵转换成一维数组的一种简单方法，
# 另一种方法是使用reshape(1,-1)