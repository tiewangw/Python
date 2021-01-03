# 清洗文本
import re

# 创建文本
text_data = [" Interrobang. By Aishwarya Henruentte      ",
             "    Parking And Going. By Karl Gautier ",
             "          Today Is The night. By Jarek Prakash"
             ]
# 去除文本两端的空格
strip_whitespace = [string.strip() for string in text_data]
print(strip_whitespace)
# ['Interrobang. By Aishwarya Henruentte', 'Parking And Going. By Karl Gautier', 'Today Is The night. By Jarek Prakash']

# 删除句点
remove_periods = [string.replace(".", "") for string in strip_whitespace]
print(remove_periods)
# ['Interrobang By Aishwarya Henruentte', 'Parking And Going By Karl Gautier', 'Today Is The night By Jarek Prakash']

# 创建自定义的转换函数
def capitalizer(string: str) -> str:
    return string.upper()
print([capitalizer(string) for string in remove_periods])
['INTERROBANG BY AISHWARYA HENRUENTTE', 'PARKING AND GOING BY KARL GAUTIER', 'TODAY IS THE NIGHT BY JAREK PRAKASH']


# 使用正则表达式函数
def replace_letters_with_X(string:str) -> str:
    return re.sub(r"[a-zA-Z]","X",string)

res = [replace_letters_with_X(string) for string in remove_periods]
print(res)
# ['XXXXXXXXXXX XX XXXXXXXXX XXXXXXXXXX', 'XXXXXXX XXX XXXXX XX XXXX XXXXXXX', 'XXXXX XX XXX XXXXX XX XXXXX XXXXXXX']



