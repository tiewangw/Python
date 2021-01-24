# 通过最大化类间可分性进行特征降维
# 使用线性判别分析（Linear Discriminant Analysis，LDA）方法，将特征数据映射到一个可以使类间可分性最大的成分坐标轴上
from sklearn import datasets
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# 加载Iris flower数据集
iris = datasets.load_iris()
features = iris.data
target = iris.target
# 创建并允许LDA，然后用它对特征做变换
lda = LinearDiscriminantAnalysis(n_components=1)
features_lda = lda.fit(features, target).transform(features)

# 打印特征数量
print("Original number of features : ", features.shape[1])
# Original number of features :  4
print("Reduced  number of features : ", features_lda.shape[1])
# Reduced  number of features :  1

# 查看每个成分保留的信息量
print(lda.explained_variance_ratio_)
# [0.9912126]