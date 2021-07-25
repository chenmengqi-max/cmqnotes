board = []
for _ in range(9):
    board.append(input().replace(' ', ''))
# print(board)
def isV(board, x, y, c):
    for i in range(9):
        if board[x][i] == c or board[i][y] == c:
            return False
    for j in range(3 * (x // 3), 3 * (x // 3) + 3):
        for k in range(3 * (y // 3), 3 * (y // 3) + 3):
            if board[j][k] == c:
                return False
    return True

num = []
for i in range(9):
    for j in range(9):
        if board[i][j] == '0':
            num.append([i, j])
q = [[board, 0]]
res = '#'
while q:
    board, idx = q.pop()
    if idx == len(num):
        res = board[:]
        break
    i, j = num[idx]
    for c in '123456789':
        if isV(board, i, j, c):
            tmp = board[i]
            cur = tmp[:j] + c + tmp[j + 1:]
            board[i] = cur
            q.append([board[:], idx + 1])
for i in range(9):
    s1 = []
    for c in res[i]:
        s1.append(c)
    print(' '.join(s1))

0 2 4 5 0 3 0 6 0
0 6 0 0 0 0 0 0 1
0 0 3 0 7 0 0 0 0
0 1 0 3 0 0 0 0 9
0 4 0 0 0 0 3 0 0
7 0 5 0 0 6 0 0 0
0 0 0 9 0 0 1 0 8
0 0 0 0 2 1 0 5 6
0 0 0 4 0 0 0 0 0


