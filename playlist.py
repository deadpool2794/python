k = int(input())
n = int(input())
g = int(input())
req = n
i = 0
for i in range(g):
    req *= n-i-1
for j in range(k-g-1):
    req *= n-i-1
print(req)