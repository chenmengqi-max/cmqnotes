"""
    @author： 上海大学-15122657陈孟琦
    @date： 2021/5/25 - 9:31
"""
key_word = ['ident', 'number', 'plus', 'minus', 'times', 'slash', 'lparen', 'rparen']
def read(strl):  # 读取文件 在每一项前加个序号
    f = open("result.txt")
    lines = f.readlines()
    for line in lines:
        # lines = f.readline()  文件指针下移,s
        strl.append(line)
    for i in range(len(strl)):
        strl[i] = str(i + 1) + strl[i]
    print('\n')
    for i in range(len(strl)):
        m = strl[i].index(',')+1
        n = len(strl[i])-2
        print(strl[i][m:n],end=' ')
    f.close()


def erreport(eroitem, emsg):  # 输入报错项、原因，直接用exit报错
    m = cknum(eroitem)
    print('第', m, '项出错了', emsg)
    exit(0)


def cknum(cknum):  # 提取序号
    n = []
    m = 0
    for i in range(len(cknum)):
        if cknum[i] == '(':
            break
        n.append(cknum[i])
    n = n[::-1]
    for i in range(len(n)):
        p = 10 ** i
        q = int(n[i])
        m = m + p * q
    return m


def ck(strl):  # 提取属性
    m = strl
    n = ''
    for i in range(len(m)):
        if m[i] == ',':
            break
        n = n + m[i]
    for i in range(len(n)):
        if n[0] == '(':
            n = n[1::]
            break
        n = n[1::]
    return n


def delparen(fullstr):  # 去掉括号
    n = []  # 记录括号位置 处理数组
    flag1 = 0
    flag2 = 0
    for i in range(len(fullstr)):
        n.append(ck(fullstr[i]))
    if n.count('lparen') != n.count('rparen'):  # 检查括号配对
        while ck(fullstr[0]) != 'lparen' and ck(fullstr[0]) != 'rparen':
            fullstr.pop(0)
        erreport(fullstr[0], '括号不匹配')
    while n.count('lparen') != 0:
        flag2 = n.index('rparen')
        n = n[flag2::-1]
        flag1 = len(n) - n.index('lparen') - 1
        n = fullstr[flag1+1:flag2]      # 选择第一个右括号与倒序最近左括号内的内容进行检验
        if len(n) == 0:
            erreport(fullstr[flag1], '括号内为空')
        fullstr = fullstr[:flag1] + expr(n) + fullstr[flag2 + 1:]
        n = []
        for i in range(len(fullstr)):
            n.append(ck(fullstr[i]))
    return fullstr


def expr(fullstr):  # 检验是否为表达式
    a = ['(ident,occupy)']
    if ck(fullstr[0]) == 'plus' or ck(fullstr[0]) == 'minus':
        fullstr.pop(0)
        item(fullstr)
    elif ck(fullstr[0]) == 'ident' or ck(fullstr[0]) == 'number':
        item(fullstr)
    else:
        erreport(fullstr[0], '表达式规约出错')
    if len(fullstr) == 0:
        return a
    while ck(fullstr[0]) == 'plus' or ck(fullstr[0]) == 'minus':
        fullstr.pop(0)
        item(fullstr)
    if len(fullstr) == 0:
        return a
    else:
        erreport(fullstr[0], '表达式太长了')


def item(fullstr):          # 检验是否为项(因子
    a = ['(ident,occupy)']
    if ck(fullstr[0]) == 'ident' or ck(fullstr[0]) == 'number':
        fullstr.pop(0)
    else:
        erreport(fullstr[0], '项不合规范')
    if len(fullstr) == 0:
        return a
    elif ck(fullstr[0]) == 'times' or ck(fullstr[0]) == 'slash':
        fullstr.pop(0)
        if ck(fullstr[0]) == 'ident' or ck(fullstr[0]) == 'number':
            fullstr.pop(0)
            return a
        else:
            erreport(fullstr[0], '项不合规范')
    elif ck(fullstr[0]) == 'plus' or ck(fullstr[0]) == 'minus':
        return fullstr
    else:
        erreport(fullstr[0], '项不合规范')
    if len(fullstr) == 0:
        return a
    else:
        erreport(fullstr[0], '项不合规范')


def main():
    fullstr = []
    read(fullstr)
    print('\n',fullstr)
    fullstr = delparen(fullstr)
    expr(fullstr)
    print(''
          ''
          '那还挺对的')


main()