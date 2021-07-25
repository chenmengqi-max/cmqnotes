"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/5/9 - 16:12
"""
while 1:
    try:
        a,b=input().split(',')
        # for i in a:
        #     if i.count()>1:
        #         print(0)
        #         break
        print(a,b)
        m = len(a)
        n = int(b)
        print(m,n)
        if(n<=m and m<=52):
            mm=1
            nn=1
            for i in range(1,m+1):
                mm=i*mm
            for i in range(1,m-n+1):
                nn=i*nn
            result = mm//nn//n
            print('*')
            print(result)
        else:
            print(0)
    except:
        break
