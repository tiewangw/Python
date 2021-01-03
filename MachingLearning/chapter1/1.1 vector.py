# 创建一个向量（vector）

import numpy as np
# 创建一个行向量
vector_row = np.array([1,2,3,4,5,6])
# 创建一个列向量
vector_rcolumn = np.array([ [1],
                            [2],
                            [3]])

print(vector_row)
# [1 2 3]
print("----------------------")


print(vector_rcolumn)
# [[1]
#  [2]
 # [3]]

print("----------------------")

# 选择向量的第3个元素
print(vector_row[2])

print("----------------------")

# 选择向量的所有元素
print(vector_row[:])

print("----------------------")

# 选择从第1个到第3个
print(vector_row[:3])

print("----------------------")

# 选择第3个之后所有
print(vector_row[3:])

print("----------------------")

# 选择最后一个
print(vector_row[-1])