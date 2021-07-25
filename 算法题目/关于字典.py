"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/4/23 - 10:43
"""

# dic1 = {'date':'2018.11.2','name':'carlber','work':"遍历",'number':3}
# for i in dic1:   #遍历字典中的键
#     print(i)
#
# for key in dic1.keys():
#     print(key)
#
# for value in dic1.values():  #遍历字典中的值
#     print(value)
#
# for item in dic1.items():  #遍历字典中的元素
#     print(item[0])
#
# for i in dic1:
#     print("该次循环得到的key为%s，得到的值为%s"%(i,dic1[i]))

def sortedDictValues1(adict):

    items = list(adict.keys())

    print("items:",items)

    items.sort()

    return [value for value in items]

adict = {"a1":11,"b1":2,"c1":30,"e1":20,"d1":4}

print(sortedDictValues1(adict))
