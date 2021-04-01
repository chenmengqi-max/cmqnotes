"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/4/1 - 12:50
"""
import csv
import matplotlib.pyplot as plt
import numpy as np
file = csv.reader(open('../heros.csv'))
zhanshishuxing=[] #战士属性列表
pingjunzhi = ["英雄属性平均值"]
x = []
y = []
hero = []
name = []
shuxing = []

for i in range(1,20):
    pingjunzhi.append(0)

for i in file:
    shuxing = i
    break
shuxing.remove("英雄")
shuxing.remove("攻击范围")
shuxing.remove("主要定位")
shuxing.remove("次要定位 ")
print(shuxing)

next(file) #略过第一行
for i in file :
    for j in range(1,20):
        pingjunzhi[j] = pingjunzhi[j] + float(i[j].strip("%"))
    if i[21] == "坦克":
        zhanshishuxing.append(i) #战士属性列表
for i in range(1,20):
    pingjunzhi[i] = pingjunzhi[i] / 69

for i in range(len(zhanshishuxing)):
    x.append(i)

print(pingjunzhi)
print(zhanshishuxing)

for i in zhanshishuxing:
    name.append(i[0])
    y = []
    for j in range(1,20):
        y.append(((float(i[j].strip("%")) / pingjunzhi[j]) - 1 )*100)
    hero.append(y)

print(hero)

# for i in range(len(zhanshishuxing)):
#     plt.plot(x,hero[i])
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
color = ['#F0F888',
'#D4F199',
'#00FFFF',
'#7FFFD4',
'#00F55F',
'#F5F5DC',
'#FFE009',
'#000000',
'#FFEBCD',
'#0000FF',
'#8A2BE2',
'#A52A2A',
'#DEB887',
'#5F9EA0',
'#7FFF00',
'#D2691E',
'#FF7F50',
'#6495ED',
'#6005ED']

for i in range(len(hero)):
    plt.plot(shuxing,hero[i],marker='o', markersize=3,color=color[i])
plt.legend(name)

plt.xlabel('不同属性')  # x轴标题
plt.ylabel('属性值--超过平均值百分比')  # y轴标题
plt.show()












#最大血量
# blood=[]
# next(file)
# file1=[]
# for i in file:
#     blood.append(int(i[1]))
#     file1.append(i)
# print(max(blood),min(blood))
# for i in file1:
#     if int(i[1]) == max(blood):
#         print(i[0],"maxblood: ",max(blood))
#     if int(i[1]) == min(blood):
#         print(i[0],"minblood: ",min(blood))


#战士
# for i in file:
#     if i[21]=="战士":
#         print(i[0])


