# 填充缺失的分类值
# 最理想的方法是训练一个机器学习分类器来预测缺失值，通常会使用KNN分类器
import numpy as np
from sklearn.neighbors import KNeighborsClassifier

# 用分类特征创建特征矩阵
X = np.array([
    [0, 2.10, 1.45],
    [1, 1.18, 1.33],
    [0, 1.22, 1.27],
    [1, -0.21, -1.19]
])
# 创建带缺失值的特征矩阵
X_with_nan = np.array([
    [np.nan, 0.87, 1.31],
    [np.nan, -0.67, -0.22]
])

# 训练KNN分类器
clf = KNeighborsClassifier(3, weights='distance')
trained_model = clf.fit(X[:, 1:], X[:, 0])
# 预测缺失值的分类
imputed_values = trained_model.predict(X_with_nan[:, 1:])
# 将所预测的分类和它们的其他特征连接起来
X_with_imputed = np.hstack((imputed_values.reshape(-1, 1), X_with_nan[:, 1:]))
# 连接2个特征矩阵
print(np.vstack((X_with_imputed, X)))
# [[ 0.    0.87  1.31]
#  [ 1.   -0.67 -0.22]
#  [ 0.    2.1   1.45]
#  [ 1.    1.18  1.33]
#  [ 0.    1.22  1.27]
#  [ 1.   -0.21 -1.19]]
