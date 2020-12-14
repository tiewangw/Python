# 对观察值进行聚类操作，是相似的观察值被分为一组

import pandas as pd
from sklearn.datasets import  make_blobs
from sklearn.cluster import KMeans
# 创建模拟的特征矩阵
features,_ = make_blobs(n_samples=50,
                         n_features=2,
                         centers=3,
                         random_state=1)
# 创建数据帧
dataframe = pd.DataFrame(features,columns=["feature_1","featrue_2"])
# 创建K-Means聚类器
clusterer = KMeans(3,random_state=0)
# 将聚类器应用在特征上
clusterer.fit(features)
# 预测聚类的值
dataframe["group"] = clusterer.predict(features)
# 查看前几个观察的值
print(dataframe.head(5))

#    feature_1  featrue_2  group
# 0  -9.877554  -3.336145      0
# 1  -7.287210  -8.353986      2
# 2  -6.943061  -7.023744      2
# 3  -7.440167  -8.791959      2
# 4  -6.641388  -8.075888      2


