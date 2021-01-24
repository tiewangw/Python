# 使用主成分进行特征降维：对于给定的一组特征，在保留信息量的同时减少特征的数量
# 使用scikit-learn库中的主成分分析工具 PCA(Principal Component Analysis)
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn import datasets

# 加载数据
digits = datasets.load_digits()
# 标准化特征矩阵
features = StandardScaler().fit_transform(digits.data)

# 创建可以保留99%信息量的PCA
# n_components ：保留的原始信息量
# whiten=True ：表示对每一个主成分都进行转换已保证它们的平均值为0，方差为1
pca = PCA(n_components=0.99,whiten=True)
# 执行PCA
features_pca = pca.fit_transform(features)

print("Original number of features : ",features.shape[1])
# Original number of features :  64
print("Reduced  number of features : ",features_pca.shape[1])
# Reduced  number of features :  54