#  将一个数值型的值缩放（rescale）到2个特定的值之间。
# 用scikit-learn的MinMaxScale来缩放一个特征数组
import numpy as np
from sklearn import preprocessing
# 创建特征
feature = np.array([
    [-500.5],
    [-100.5],
    [0],
    [100.5],
    [-500.5]
])
# 创建缩放器
minmax_sacle = preprocessing.MinMaxScaler(feature_range=(0,1))

# 缩放特征的值
scaled_feature = minmax_sacle.fit_transform(feature)

print(scaled_feature)
# [[0.       ]
#  [0.6655574]
#  [0.8327787]
#  [1.       ]
#  [0.       ]]



