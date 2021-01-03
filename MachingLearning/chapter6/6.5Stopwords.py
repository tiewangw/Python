# 删除停止词:给定一组分好词的文本数据，删除其中非常常见但包含的信息又很少的单词（如：is、of、and）。

from nltk.corpus import stopwords
# 如果是第一次使用停止词集，需要先下载
# import nltk
# nltk.download('stopwords')

tokenized_words = ['i',
                   'am',
                   'going',
                   'to',
                   'go',
                   'to',
                   'the',
                   'store',
                   'and',
                   'park']
# 加载停止词集
stop_words = stopwords.words('english')
# 删除停止词
res = [word for word in tokenized_words if word not in stop_words]
print(res)
# ['going', 'go', 'store', 'park']

# 查找并删除单词序列中的停止词
print(stop_words[:15])
# ['i', 'me', 'my', 'myself', 'we']
