# 数值型特征方差的阈值化
from sklearn import  datasets
from sklearn.feature_selection import VarianceThreshold
# 加载数据
iris = datasets.load_iris()
# 创建features和target
features = iris.data
target = iris.target
# 创建VarianceThreshold对象
thresholder = VarianceThreshold(threshold=.5)
# 显示方差
print(thresholder.fit(features).variances_)
# [0.68112222 0.18871289 3.09550267 0.57713289]
# 创建大方差特征矩阵
features_high_variance = thresholder.fit_transform(features)
# 显示大方差特征矩阵
print(features_high_variance[:3])
# [[5.1 1.4 0.2]
#  [4.9 1.4 0.2]
#  [4.7 1.3 0.2]]
