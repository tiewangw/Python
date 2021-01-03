# 将文本分离成独立的单词或句子
# NLTK(Natural Language Toolkit)Python的自然语言工具集


# 报错NLTK：Resource punkt not found. Please use the NLTK Downloader to obtain the resource处理方式
# https://blog.csdn.net/m0_49672766/article/details/111995053)


from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize

string = "The science of today is the technology of tomorrow"
print(word_tokenize(string))
# ['The', 'science', 'of', 'today', 'is', 'the', 'technology', 'of', 'tomorrow']

string = "The science of today is the technology of tomorrow. Tomorrow is Today"
print(sent_tokenize(string))
# ['The science of today is the technology of tomorrow.', 'Tomorrow is Today']


