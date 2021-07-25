"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/5/27 - 19:23
"""
n = int(input())
pai = input().split()
count = 0
count2=0
count3 = 0
count4 = 0
for i in pai:
    if pai.count(i) == 4:
        count += 1
        count4 +=1
        for _ in range(4):
            pai.remove(i)
    elif pai.count(i) == 2:
        count += 1
        count2 += 1
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
yu2 = 0
yu3 = 0
if count1 > count3:
    count1 = count1 - count3
else:
    count1 = 0
    yu = count3 - count1
    yu2 = yu // 2
    yu = yu - yu2*2
    yu3 = yu // 3
result = count + count1
result -= yu2
result -= yu3
print(result)
