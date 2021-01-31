# 有一组二值特征数据（即只有两个分类），移除其中方差较小的特征
from sklearn.feature_selection import VarianceThreshold
# 创建特征
features = [
    [0,1,0],
    [0,1,1],
    [0,1,0],
    [0,1,1],
    [1,0,0]
]
# 创建VarianceThreshold对象
thresholder = VarianceThreshold(threshold=(0.75 * (1 - 0.75)))

print(thresholder.fit_transform(features))
# [[0]
#  [1]
#  [0]
#  [1]
#  [0]]



