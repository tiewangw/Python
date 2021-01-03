# 创建一组特征来表示观察值文本中包含的特定单词的数量
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer

text_data = np.array(
    ['I love Brazil. Brazil!',
     'Sweden is best',
     'Germany beats both']
)
# 创建一个词袋特征矩阵
count = CountVectorizer()
bag_of_words = count.fit_transform(text_data)

print(bag_of_words)
# (0, 6)    1
# (0, 3)    2
# (1, 7)    1
# (1, 5)    1
# (1, 1)    1
# (2, 4)    1
# (2, 0)    1
# (2, 2)    1

# 查看每个观察值的词频统计矩阵
print(bag_of_words.toarray())
# [[0 0 0 2 0 0 1 0]
#  [0 1 0 0 0 1 0 1]
#  [1 0 1 0 1 0 0 0]]

# 查看特征名
print(count.get_feature_names())
['beats', 'best', 'both', 'brazil', 'germany', 'is', 'love', 'sweden']