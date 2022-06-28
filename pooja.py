def solve(N):
    N = sorted(N)
    p1 , p2 = "", ""
    for i in range(len(N)):
        if(i&1): 
            p1 += N[i]
        else :
            p2 += N[i]
    print(p1,p2)
    return int(p1)+ int(p2)


# T = int(input())
# for _ in range(T):
#     N = input()

#     out_ = solve(N)
#     print(out_)



# t = int(input())
# for _ in range(t):
#     n = int(input())
#     arr = input().split()
#     q = int(input())
#     for _ in range(q):
#         a,b,c = input().split()
#         if(a == '1'):
#             arr.reverse()
#         elif(a == '2'):
#             b,c = int(b)-1, int(c)-1
#             p, q= arr[b], arr[c]
#             arr[b], arr[c] = q, p
#         else:
#             print(arr.index(b) + 1)
#         print(arr)
        
# input1 = sorted(input())
# input2 = sorted(input())
# print("yes") if(input1 == input2) else print("no")


def maxElement(cls, input1):
    d = {}
    for i in input1:
        try:
            d[i] += 1
        except:
            d[i] = 1
    mx, alph = 0 , ""
    for k,v in d.items():
        if v > mx:
            mx = v
            alph = k
    mx_freq = 0
    for k,v in d.items():
        if v == mx:
            mx_freq += 1
    if(mx_freq > 1):
        return "0"
    return alph




# input1 = [int(i) for i in input().split()]
# input1.append(0)
# res = []
# for i in range(len(input1)-1):
#     if(input1[i] != input1[i+1]):
#         res.append(input1[i])
# print(res)


def characterAt( input1, input2):
    string = ""
    for i in range(0,len(input1),2):
        string += input1[i] * int(input1[i+1])
    if(len(string) < input2):
        return "-1"
    return string[input2-1]

# input1 = input()
# input2 = int(input())
# print(characterAt(input1, input2))

    # blueCars = []
    # for i in range(input1):
    #     for j in range(input2):
    #         if input3[i][j] == 1:
    #             blueCars.append((True,i,j))
    
    # cords = [(-1,0), (1,0), (0,-1), (0,1)]
    # for i in range(len(blueCars)) :
    #     row, col = blueCars[i][1], blueCars[i][2]
    #     blueCars[i][0] = False
    #     for m,n in cords:
    #         row_ =row + m
    #         col_ =col + n
    #         if(row_ >= input1 or col_ >= input2 or row_ < 0 or col_ < 0 or input3[row_][col_] != 1):
    #             continue
            
    #         if(blueCars[row_][col_]):
def connectedComponents(row, col,input3, visited, ct):
    if (row >= len(input3) or row < 0 or col >= len(input3[0]) or col < 0):
        return
    
    if(visited[row][col]):
        return
    



        
def findPatch( input1, input2, input3):
    visited = []
    for i in range(input1):
        aux = [False] * input2
        visited.append(aux)
    ct = 0
    patches = connectedComponents(0, 0, input3, visited, ct)
    return patches




# input1 = int(input())
# input2 = int(input())
# input3 = []
# for i in range(input1):
#     aux = [int(x) for x in input().split()]
#     input3.append(aux)

# print(findPatch(input1, input2, input3))

tc = int(input())
for _ in range(tc):
    n = int(input())
    arr = [int(x) for x in input().split()][:n]
    mx , mn = 0, 10000001
    mxInd, mnInd = 0,0 
    for i in range(len(arr)):
        if(mx < arr[i]):
            mx = arr[i]
            mxInd = i
        if mn > arr[i]:
            mn = arr[i]
            mnInd = i 
   
    ans = mnInd
    ans += n-1-mxInd
    if(mxInd < mnInd):
        ans -= 1
    print(ans)


    
























