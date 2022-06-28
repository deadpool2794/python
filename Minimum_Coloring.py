def check(num, x, y):
    if mat[x][y+1] != num and mat[x-1][y] != num and mat[x][y-1] != num and mat[x+1][y] != num:
        return True
    return False


def fillMat(mat, x, y, n, m):
    
    if (x == 0 or y == 0 or x == n+1 or y == m+1 ):
        return
    for i in range(1, 4):
        if check(i, x, y):
            mat[x][y] = i
            if(mat[x][y+1] == 0):
                fillMat(mat, x, y+1, n, m)
            mat[x][y+1] = 0
            if(mat[x][y-1] == 0):
                fillMat(mat, x, y-1, n, m)
            mat[x][y-1] = 0
            if(mat[x+1][y] == 0):
                fillMat(mat, x+1, y, n, m)
            mat[x+1][y] = 0
            if(mat[x-1][y] == 0):
                fillMat(mat, x-1, y, n, m)
            mat[x-1][y] = 0


t = int(input())
for _ in range(t):
    n, m = [int(x) for x in input().split()]
    x1, y1 = [int(x) for x in input().split()]
    x2, y2 = [int(x) for x in input().split()]
    mat = []
    for i in range(n+2):
        row = []
        for j in range(m+2):
            row += [0]
        mat.append(row)
    mat[x1][y1] = 1
    mat[x2][y2] = 2
    
    fillMat(mat, x1, y1, n, m)
    print(mat)




























