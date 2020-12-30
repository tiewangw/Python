# 移除标点
import unicodedata
import sys

# 创建文本
text_data = ['Hi!!!!! I. lOVE. This. Song .....',
             '1000% Agree!!!  #LoveIT']
# 创建一个标点字典
punctuation = dict.fromkeys(i for i in range(sys.maxunicode)
                            if unicodedata.category(chr(i)).startswith('P'))
# 移除每个字符串中的标点
res = [string.translate(punctuation) for string in text_data]

print(res)
# ['Hi I lOVE This Song ', '1000 Agree  LoveIT']
