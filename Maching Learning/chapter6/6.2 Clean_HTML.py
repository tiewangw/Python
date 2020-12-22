
# 解析并清洗HTML
from bs4 import BeautifulSoup

html = """
    <div class='full_name'><span style='font-weight:bold'>
    Masego Azra
"""
# 解析HTML
soup = BeautifulSoup(html,"lxml")
# 查找class是full_name的div标签，并查看文本
res = soup.find("div",{"class":"full_name"}).text

print(res)