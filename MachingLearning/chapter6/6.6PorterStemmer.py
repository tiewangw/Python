# 提取词干：将一个单词序列中的单词转换成它们的词干
# 词干提起(stemming)能识别出一个单词的词缀并将其删除（例如，动名词中的ing），同时保留其词根的意思。

from nltk.stem.porter import PorterStemmer

# 单词序列
tokenized_words = ['i',  'am', 'hunbled', 'by','this','traditional','meeting']
# 创建词干转换器
porter = PorterStemmer()
# 应用词干转换器
res = [porter.stem(word) for word in tokenized_words]
print(res)
# ['i', 'am', 'hunbl', 'by', 'thi', 'tradit', 'meet']