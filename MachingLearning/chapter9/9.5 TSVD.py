# 对稀疏数据矩阵进行降维
# 使用截断奇异值分解法（Truncated Singular Value Decomposition,TSVD)
from scipy.sparse import csr_matrix
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import StandardScaler
from sklearn import datasets
# 加载数据
digits = datasets.load_digits()
# 加载特征数据
features = StandardScaler().fit_transform(digits.data)
# 加载稀疏矩阵
features_sparse = csr_matrix(features)
# 创建TSVD
tsvd = TruncatedSVD(n_components=10)
# print(tsvd)
# TruncatedSVD(algorithm='randomized', n_components=10, n_iter=5,random_state=None, tol=0.0)

features_sparse_tsvd = tsvd.fit(features_sparse).transfrom(features_sparse)
print(features_sparse_tsvd)

# AttributeError: 'TruncatedSVD' object has no attribute 'transfrom'


# print("Original number of features:",features_sparse.shape[1])
# print("Reduced number of features:",features_sparse_tsvd.shape[1])
# Original number of features: 64
# Reduced number of features: 10
