# 计算数组的一些描述性统计值
import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

# 返回平均值
print(np.mean(matrix))  # 5

# 返回方差
print(np.var(matrix))  # 6.666666666666667

# 返回标准差
print(np.std(matrix))  # 2.581988897471611
print("----------------")

# 返回每一列的平均值
print(np.mean(matrix,axis=0))  # [4. 5. 6.]