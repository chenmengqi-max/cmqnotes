"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/5/27 - 20:37
"""
n = int(input())
pai = input().split()
count = 0
count3 = 0
for i in pai:
    if pai.count(i) == 4:
        count += 1
        for _ in range(4):
            pai.remove(i)
    elif pai.count(i) == 2:
        count += 1
        for _ in range(2):
            pai.remove(i)
    elif pai.count(i) == 3:
        count += 1
        count3 += 1
        for _ in range(3):
            pai.remove(i)
    else:
        pass
count1 = len(pai)
if count1 > count3:
    count1 = count1 - count3
else:
    count1 = 0
yu2 = count3-count1//2
if count3-count1//2 > 0:
    count-=yu2
result = count + count1
print(result)