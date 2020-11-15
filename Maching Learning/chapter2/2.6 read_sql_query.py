# 查询sql数据库

import pandas as pd
from sqlalchemy import create_engine

# 创建数据库连接
database_connection = create_engine('sqlite:///sample.db')
# 加载数据
dataframe = pd.read_sql_query('select * from data', database_connection)

print(dataframe.head(2))
