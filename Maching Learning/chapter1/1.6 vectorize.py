# vectorize :对一个数组中的多个元素同事使用某个函数
import numpy as np

matrix = np.array([
    [1,2,3],
    [1,2,3],
    [1,2,3]
])

# 创建一个函数，返回输入值加上100以后的值
add_100 = lambda i:i+100

# 创建向量化函数
vectorized_add_100 = np.vectorize(add_100)
# 对矩阵的所有元素应用这个函数
print(vectorized_add_100(matrix))
print("------------------------")

# vectorize本质上对所有元素循环执行某个操作，所以不会提升性能
# 使用Numpy是广播方法（broadcasting）：对两个维度不通的数组执行操作，更简单。
print(matrix+100)