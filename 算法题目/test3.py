"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/5/27 - 19:38
"""
import copy

n,k=map(int,input().split())
arr = list(map(int,input().split()))
count = 0
for i in range(0,n-k+1):
    temp = arr[i:i+k:]
    temp2 = copy.deepcopy(temp)
    temp.sort()
    arr = arr[:i:]+temp+arr[i+k::]
    zhong = (2*i+k-1) // 2
    count += arr[zhong]
    arr = arr[:i:]+temp2+arr[i+k::]
print(count)