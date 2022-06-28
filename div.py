mat = [[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
n = 4
for i in range(n-1):
    for j in range(n-i-1):
        print(mat[i][j], end = ' ')
    print()

