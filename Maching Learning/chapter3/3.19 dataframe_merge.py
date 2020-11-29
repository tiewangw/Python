# 合并2个数据帧

import pandas as pd

employee_data = {'employee_id': ['1', '2', '3', '4'],
                 'name': ['Amy', 'Allen', 'Alice', 'Tim']}
dataframe_employees = pd.DataFrame(employee_data, columns=['employee_id', 'name'])

sale_data = {'employee_id': ['3', '4', '5', '5'],
             'total_sales': [115, 558, 8889, 887]}
dataframe_sales = pd.DataFrame(sale_data, columns=['employee_id', 'total_sales'])

# --------------合并 ，merge默认进行等值连接 inner join
df = pd.merge(dataframe_employees, dataframe_sales, on='employee_id')
print(df)
#   employee_id   name  total_sales
# 0           3  Alice          115
# 1           4    Tim          558

# -----------外连接 outer join
df = pd.merge(dataframe_employees, dataframe_sales, on='employee_id',how='outer')
print(df)
#   employee_id   name  total_sales
# 0           1    Amy          NaN
# 1           2  Allen          NaN
# 2           3  Alice        115.0
# 3           4    Tim        558.0
# 4           5    NaN       8889.0
# 5           5    NaN        887.0

