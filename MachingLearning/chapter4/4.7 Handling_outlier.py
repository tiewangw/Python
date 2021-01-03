# 处理异常值  :  通常使用第3种方法来处理异常值

import pandas as pd
import numpy as np

houses = pd.DataFrame()
houses['Price'] = [23232, 4434, 542, 2323]
houses['Bathrooms'] = [2, 5, 3.5, 44]
houses['Square_Feet'] = [1500, 2500, 1400, 23232]

# 方法1：筛选观察值
print(houses[houses['Bathrooms'] < 20])
#    Price  Bathrooms  Square_Feet
# 0  23232        2.0         1500
# 1   4434        5.0         2500
# 2    542        3.5         1400


# 方法2 将他们标记为特征值，并作为数据的一个特征
houses['Outlier'] = np.where(houses['Bathrooms'] < 20, 0, 1)
print(houses)
#    Price  Bathrooms  Square_Feet  Outlier
# 0  23232        2.0         1500        0
# 1   4434        5.0         2500        0
# 2    542        3.5         1400        0
# 3   2323       44.0        23232        1


# 方法3  对有异常值的特征进行转换，降低异常值的影响
houses["Log_of_Square_Feet"] = [np.log(x) for x in houses["Square_Feet"]]
print(houses)
#    Price  Bathrooms  Square_Feet  Outlier  Log_of_Square_Feet
# 0  23232        2.0         1500        0            7.313220
# 1   4434        5.0         2500        0            7.824046
# 2    542        3.5         1400        0            7.244228
# 3   2323       44.0        23232        1           10.053286
