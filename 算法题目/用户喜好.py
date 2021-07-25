"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/5/27 - 9:20m
"""
while(1):
    try:
        n = int(input())
        user = list(map(int,input().split()))
        q = int(input())
        for i in range(q):
            l,r,k = map(int,input().split())
            count = 0
            for i in range(l-1,r):
                if user[i] == k:
                    count += 1
            print(count)
    except:
        break

