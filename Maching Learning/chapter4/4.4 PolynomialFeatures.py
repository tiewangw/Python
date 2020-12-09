# 创建多项式特征和交互特征

import numpy as np
from sklearn.preprocessing import  PolynomialFeatures

# 创建特征矩阵
featrues = np.array([
    [2,3],
    [2,3],
    [2,3]
])

# 创建PolynomialFeatures对象
# degree参数决定了多项式的最高阶数
ploynomial_interaction = PolynomialFeatures(degree=2,include_bias=False)
# 创建多项式特征
pol = ploynomial_interaction.fit_transform(featrues)

print(pol)
# [[2. 3. 4. 6. 9.]
#  [2. 3. 4. 6. 9.]
#  [2. 3. 4. 6. 9.]]