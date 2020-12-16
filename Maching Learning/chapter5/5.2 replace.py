# 对ordinal分类特征编码
# 创建一个字典，将分类的字符串标签映射为一个数字，然后将其映射在特征上
import pandas as pd
# 创建特征
dataframe = pd.DataFrame({"Score": ["Low", "Low", "Medium", "Medium", "High"]})

# 创建映射器
scaler_mapper = {"Low": 1,
                 "Medium": 2,
                 "High": 3}
# 使用映射器来替换特征
res = dataframe["Score"].replace(scaler_mapper)
print(res)
# 0    1
# 1    1
# 2    2
# 3    2
# 4    3
# Name: Score, dtype: int64
