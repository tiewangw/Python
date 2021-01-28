# 对非负特征矩阵进行降维
# 使用(Non-Negative Matrix Factorization,NMF)非负矩阵分解法
from sklearn.decomposition import NMF
from sklearn import datasets
# 加载数据
digits = datasets.load_digits()
# 加载特征数据
features = digits.data
# 创建NMF，进行变换并应用
nmf = NMF(n_components=10,random_state=1)
features_nmf = nmf.fit_transform(features)

print("Original number of features:",features.shape[1])
print("Reduced number of features:",features_nmf.shape[1])
# Original number of features: 64
# Reduced number of features: 10
