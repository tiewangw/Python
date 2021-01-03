import numpy as np

# 设置随机数种子
np.random.seed(0)

# 生成3个0.0 到1.0 之间的随机浮点数
num = np.random.random(3)
print(num)

# 生成3个1到10之间的随机整数
num = np.random.randint(0,11,3)
print(num)

# 从大于或等于1.0并且小于2.0的范围中抽取3个数
num = np.random.uniform(1.0,2.0,3)
print(num)
