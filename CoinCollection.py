def collect(i, j, n):
    if i < 0 or j < 0 or i >=n or j >= n:
        return 0
    if board[i][j] == 'N' or isVisited[i][j] == 1:
        return 0
    isVisited[i][j] = 1
    ct = 1
    ct += collect(i-1, j, n)
    ct += collect(i+1, j, n)
    ct += collect(i, j+1, n)
    ct += collect(i, j-1, n)
    return ct


n = int(input())
board = []
isVisited = []
for i in range(n):
    row = list(input())
    board.append(row)
    isVisited.append([0]*n)
groups = []
for i in range(n):
    for j in range(n):
        if board[i][j] != 'N' and isVisited[i][j] == 0:
            group = collect(i, j, n)
            if group!= 0:
                groups.append(group)
player1 = 0
player2 = 0
groups.sort(reverse=True)
for i in range(len(groups)):
    if i % 2 == 0:
        player1 += groups[i]
    else:
        player2 += groups[i]

print(player1, player2)