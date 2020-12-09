# 对观察值的每一个特征进行缩放，使其拥有一致的范数（总长度是1）
# 范数(norm)是数学中的一种基本概念。
#         在泛函分析中，它定义在赋范线性空间中，并满足一定的条件， 即①非负性；②齐次性；③三角不等式。
#         它常常被用来度量某个向量空间（或矩阵）中的每个向量的长度或大小。

# 解决方案： 使用Mormalizer并制定norm参数

import numpy  as np
from sklearn.preprocessing import  Normalizer

features = np.array([
    [0.5,0.5],
    [1.1,3.4],
    [1.5,20.2],
    [1.63,34.4],
    [10.9,3.3]
])

# 创建归一化器
normalizer = Normalizer(norm="l2")

#转换特征矩阵
print(normalizer.transform(features))