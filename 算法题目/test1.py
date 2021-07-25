"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/5/27 - 19:02
"""
arr = input().split()
yuan=['a','A','e','E','I','i','O','o','U','u']
for i in range(0,len(arr)):
    if arr[i][0] in yuan:
        arr[i] = arr[i] + 'pdd'
    else:
        temp = arr[i][0]
        arr[i] = arr[i][1::]
        arr[i] = arr[i] + temp
        arr[i] = arr[i] + 'pdd'
    for j in range(i+1):
        arr[i] = arr[i] + 'a'
for i in arr:
    print(i,end=' ')