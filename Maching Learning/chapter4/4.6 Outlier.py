# 识别样本中的异常值

# import  numpy as np
from sklearn.covariance import EllipticEnvelope
from sklearn.datasets import  make_blobs

# 创建模拟数据
features,_ = make_blobs(n_samples=10,
                        n_features=2,
                        centers=1,
                        random_state=1)
# print("features : "+features)

# 将第一个观察值的值替换为极端值
features[0,0] = 10000
features[0,1] = 10000
# 创建识别器 （contamination ：污染指数）
outlier_detector  = EllipticEnvelope(contamination=.1)
# 拟合识别器
outlier_detector.fit(features)
# 预测异常值
od = outlier_detector.predict(features)

print(od)
# [-1  1  1  1  1  1  1  1  1  1]