# 数据中存在缺失值，我们希望填充或者去测这些值

import numpy as np
from fancyimpute import KNN
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_blobs

# 创建模拟特征举证
features,_ = make_blobs(n_features=2,
                        n_samples=1000,
                        random_state=1)
# 标准化特征
scaler = StandardScaler()
standardized_features = scaler.fit_transform(features)
# 将第一个特征向量的第一个值替换为缺失值
true_value = standardized_features[0,0]
standardized_features[0,0] = np.nan
# 预测特征举证中的缺失值
features_knn_imputed = KNN(K=5,verbose=0).complete(standardized_features)

# 对比真实值和填充值
print("True_value : ",true_value)
print("Imputed Value :",features_knn_imputed[0,0])
