n = int(input())
mat = []
for i in range(1, n+1):
    row = []
    for j in range(1, n+1):
        row.append(str(i)+str(j))
    mat.append(row)

inarr = [i for i in input().split(',')]

string = input()

req = []
i, j = 0, 0
for direc in string:
    if direc == "N":
        i -= 1
        if mat[i][j] not in inarr:
            if i >= 0 and j >= 0:
                req.append(mat[i][j])
            else:
                i += 1
        else:
            i+=1
    elif direc == "S":
        i += 1
        if mat[i][j] not in inarr:
            if i >= 0 and j >= 0:
                req.append(mat[i][j])
            else:
                i -= 1 
        else:
            i -= 1
    elif direc == "W":
        j -= 1
        if mat[i][j] not in inarr:
            if i >= 0 and j >= 0:
                req.append(mat[i][j])
            else:
                j+=1
        else:
            j+=1
    else:
        j += 1
        if mat[i][j] not in inarr:
            if i >= 0 and j >= 0:
                req.append(mat[i][j])
            else:
                j-=1
        else:
            j -= 1
    if i == n-1 and j == n-1:
        break
print(req)

