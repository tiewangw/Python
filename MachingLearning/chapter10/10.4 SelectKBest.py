# 删除与分类任务不相关的特征

from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2, f_classif
from sklearn.feature_selection import SelectPercentile

# 加载数据
iris = load_iris()
features = iris.data
target = iris.target
# 将分类数据转换成整数型数据
features = features.astype(int)
# 选择卡方统计量较大的两个特征
chi2_selector = SelectKBest(chi2,k=2)
features_kbest = chi2_selector.fit_transform(features,target)

print("Original number of features:" ,features.shape[1])
print("Reduced number of features:" ,features_kbest.shape[1])
# Original number of features: 4
# Reduced number of features: 2

# 选择F值最大的特征
fvalue_selector = SelectKBest(f_classif,k=2)
features_kbest = fvalue_selector.fit_transform(features,target)
print("Original number of features:" ,features.shape[1])
print("Reduced number of features:" ,features_kbest.shape[1])
# Original number of features: 4
# Reduced number of features: 2

# 选择F值位于前75%的特征
fvalue_selector = SelectPercentile(f_classif,percentile=75)
features_kbest = fvalue_selector.fit_transform(features,target)
print("Original number of features:" ,features.shape[1])
print("Reduced number of features:" ,features_kbest.shape[1])
# Original number of features: 4
# Reduced number of features: 3