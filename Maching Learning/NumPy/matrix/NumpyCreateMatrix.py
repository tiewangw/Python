import numpy as np
# 创建一个矩阵
matrix = np.array([ [1,2],
                            [1,2],
                            [1,2]])

print(matrix)

print("------------------------------------")
# Numpy提供了专门的数据结构来表示矩阵，但是不推荐使用，因为：
#   1、实际上数组才是Numpy的标准数据结构，
#   2、绝大多数Numpy返回的是数组而不是矩阵对象
matrix_object = np.mat([
    [1,2],
    [1,2],
    [1,2]
])

print(matrix_object)
print("-------------------------")

# 选择矩阵的第2行第2列
print(matrix_object[1,1])
print("-------------------------")

# 选择矩阵的第1行和第2行以及所有列
print(matrix_object[:2,:])
print("-------------------------")

# 选择矩阵的所有行和 第2列
print(matrix_object[:,1:2])




