# 对词袋模型中的词按照其在观察值中的重要程度进行加权
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer

text_data = np.array(
    ['I love Brazil. Brazil!',
     'Sweden is best',
     'Germany beats both']
)
# 创建TF-IDF特征矩阵
tfidf = TfidfVectorizer()
feature_matrix = tfidf.fit_transform(text_data)

print(feature_matrix)
# (0, 3)  0.8944271909999159
# (0, 6)  0.4472135954999579
# (1, 1)  0.5773502691896257
# (1, 5)  0.5773502691896257
# (1, 7)  0.5773502691896257
# (2, 2)  0.5773502691896257
# (2, 0)  0.5773502691896257
# (2, 4)  0.5773502691896257

# 查看TF-IDF特征矩阵的稠密矩阵形式
print(feature_matrix.toarray())
# [[0.         0.         0.         0.89442719 0.         0.         0.4472136  0.        ]
#  [0.         0.57735027 0.         0.         0.         0.57735027 0.         0.57735027]
#  [0.57735027 0.         0.57735027 0.         0.57735027 0.         0.         0.        ]]

# 查看特征的单词表
print(tfidf.vocabulary_)
# {'love': 6, 'brazil': 3, 'sweden': 7, 'is': 5, 'best': 1, 'germany': 4, 'beats': 0, 'both': 2}