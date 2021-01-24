# 对线性不可分数据进行特征降维
# 使用sKernel PCA
from sklearn.decomposition import PCA,KernelPCA
from sklearn.datasets import make_circles

# 创建线性不可分数据
features,_ = make_circles(n_samples=1000,
                          random_state=1,
                          noise=0.1,
                          factor=0.1)
# 应用基于径向基函数（Radius Basis Function, RBF)核的Kernel PCA方法
kpca = KernelPCA(kernel="rbf",
                 gamma=15,
                 n_components=1)
features_kpca = kpca.fit_transform(features)

print("Original number of features : ",features.shape[1])
# Original number of features :  2
print("Reduced  number of features : ",features_kpca.shape[1])
# Reduced  number of features :  1