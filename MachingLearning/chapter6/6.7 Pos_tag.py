# 为文本数据找那个的每个单词或字符标注词性
from nltk import pos_tag
from nltk import word_tokenize

# 创建文本
text_data = "Chris loved outdoor running"


# 使用预训练的词性标注器
# text_tagged =word_tokenize(text_data)
# ['Chris', 'loved', 'outdoor', 'running']
text_tagged = pos_tag(word_tokenize(text_data))

print(text_tagged)
