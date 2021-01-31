# 处理高度相关性的特征
import pandas as pd
import numpy as np
# 创建一个特征矩阵，其中包含两个高度相关的特征
features = np.array([
    [1,1,1],
    [2,2,0],
    [3,3,1],
    [4,4,0],
    [5,5,1],
    [6,6,0],
    [7,7,1],
    [8,7,0],
    [9,7,1]
])
# 将特征矩阵转换成DataFrame
dataframe = pd.DataFrame(features)
# 创建相关矩阵
corr_matrix = dataframe.corr().abs()

print(dataframe.corr())
#           0         1         2
# 0  1.000000  0.976103  0.000000
# 1  0.976103  1.000000 -0.034503
# 2  0.000000 -0.034503  1.000000

# 选择相关矩阵的上三角阵
upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape),k=1).astype(np.bool))
print(upper)
#     0         1         2
# 0 NaN  0.976103  0.000000
# 1 NaN       NaN  0.034503
# 2 NaN       NaN       NaN

# 找到相关性大于0.95的特征列的索引
to_drop = [column for column in upper.columns if any(upper[column] > 0.95)]
# 删除特征
print(dataframe.drop(dataframe.columns[to_drop],axis=1))

#    0  2
# 0  1  1
# 1  2  0
# 2  3  1
# 3  4  0
# 4  5  1
# 5  6  0
# 6  7  1
# 7  8  0
# 8  9  1