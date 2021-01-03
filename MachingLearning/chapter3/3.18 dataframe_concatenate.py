# 连接2个数据帧

import pandas as pd

data_a = {'id':['1','2','3'],
          'first':['Alex','Amy','Ali'],
            'last':['Anderson','Ackerman','Allen']}
datafram_a = pd.DataFrame(data_a,columns=['id','first','last'])


data_b = {'id':['4','5','6'],
          'first':['Billy','Brain','Bran'],
            'last':['Bonder','Black','Balwner']}
datafram_b = pd.DataFrame(data_b,columns=['id','first','last'])


# --------------------按行的方向连接连个数据帧
df = pd.concat([datafram_a,datafram_b],axis=0)
print(df)
#   id  first      last
# 0  1   Alex  Anderson
# 1  2    Amy  Ackerman
# 2  3    Ali     Allen
# 0  4  Billy    Bonder
# 1  5  Brain     Black
# 2  6   Bran   Balwner


# -----------------按列的方向连接连个数据帧
df = pd.concat([datafram_a,datafram_b],axis=1)
print(df)
#   id first      last id  first     last
# 0  1  Alex  Anderson  4  Billy   Bonder
# 1  2   Amy  Ackerman  5  Brain    Black
# 2  3   Ali     Allen  6   Bran  Balwner

# 附加一行
row = pd.Series([10,'Chris','Chillon'],index=['id','first','last'])
df = datafram_b.append(row,ignore_index=True)
print(df)
#    id  first     last
# 0   4  Billy   Bonder
# 1   5  Brain    Black
# 2   6   Bran  Balwner
# 3  10  Chris  Chillon
