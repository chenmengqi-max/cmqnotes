"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/5/27 - 18:34
"""
a = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]
b = a[0]
for j in range(0, len(b)+len(a)):
    i = 0
    while (i >= 0 and j >= 0 and i<len(a) and j<len(b)):
        print(a[i][j])
        j -= 1
        i += 1
for i in range(1,len(b)):
    j = len(b)-1
    while(i < len(a)):
        print(a[i][j])
        j -= 1
        i += 1
