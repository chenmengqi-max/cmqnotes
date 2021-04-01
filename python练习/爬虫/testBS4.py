"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/3/27 - 14:39
"""
from bs4 import BeautifulSoup

file = open("test1.html","rb")
html = file.read()
bs = BeautifulSoup(html,"html.parser")
# print(bs.title)  #1.Tag 标签及其内容，但是只能拿到找到的第一个内容。
# print(bs.title.string)#2.NavigableString，标签里的内容。但输出内容不包含注释符号。
# print(bs.a.attrs)#获取一个标签里的所有的属性
#
# print(type(bs)) #3.BeautifulSoup  表示整个文档
# print(bs)

#文档的遍历
# print(bs.head.contents) #contents获取Tag的所有子节点，返回一个list
# print(bs.head.contents[1])  #按照列表序号来提取

#文档的搜索
#(1)find_all（）
#字符串过滤：会查找与字符串完全匹配的内容。
# t_list = bs.find_all("a")
# print(t_list)

#正则表达式搜索：使用search（）方法来匹配内容
# import re
# t_list = bs.find_all(re.compile("a"))
# print(t_list)

#方法：传入一个函数（方法），根据函数的要求来搜索
def name_is_exists(tag):
    return tag.has_attr("name")
t_list = bs.find_all(name_is_exists)
print(t_list)