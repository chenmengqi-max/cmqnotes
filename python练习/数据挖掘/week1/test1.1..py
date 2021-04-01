"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/4/1 - 20:42
"""

import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 显示汉字
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号
a=[1,2,3,4,5]
b=[11,21,31,41,51]
c=[21,22,23,24,25]
d=[41,21,43,14,1]

plt.plot(c,d,color = 'g')
plt.plot(a,b,color = 'r')

plt.legend(['我是红线',"我是绿线"])
plt.show()
