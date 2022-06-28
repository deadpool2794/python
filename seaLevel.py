n = int(input())

arrList = input().split()
arr = []
for i in range(n):
    arr += [int(arrList[i])]


maxi = max(arr)
mini = min(arr)
print(maxi + mini)