# 删除带有缺失值的观察值

import numpy as np
import pandas as pd

features = np.array([
    [1.1, 11.1],
    [2.2, 22.2],
    [3.3, 33.3],
    [4.4, 44.4],
    [np.nan, 55]
])

# 方法1
#  只保留没有（用~来表示）缺失值的观察值
feature = features[~np.isnan(features).any(axis=1)]
print(feature)
# [[ 1.1 11.1]
#  [ 2.2 22.2]
#  [ 3.3 33.3]
#  [ 4.4 44.4]]

# 方法2 使用pandas丢弃缺失值
dataframe = pd.DataFrame(features, columns=["feature_1", "feature_2"])
print(dataframe.dropna())
#    feature_1  feature_2
# 0        1.1       11.1
# 1        2.2       22.2
# 2        3.3       33.3
# 3        4.4       44.4