# h, w = input().split()
# n = int(input())
# d1 = {}
# for i in h+w:
#     try:
#         d1[i] += 1
#     except:
#         d1[i] = 1

# buildingNames = input().split()

# flag = False

# for name in buildingNames:
#     d = {}
#     for i in name:
#         try:
#             d[i] += 1
#         except:
#             d[i] = 1

#     for key, value in d.items():
#         try:
#             if(d1[key] < value):
#                 flag = True
#                 break
#         except:
#             flag = True
#             break
# if(flag):
#     print("NO")
# else:
#     print("YES")

# n = int(input())
# arr = [int(x) for x in input().split()]
# if(sum(arr) % 4 != 0):
#     print(-1)
# else:
#     aux = [x for x in arr if(x%4 != 0)]
#     d = {}
#     d[1], d[2],d[3] = 0, 0, 0
#     for i in aux:
#         d[i%4] += 1

#     if d[2] %2 != 0 or d[1] != d[3]:
#         print(-1)
#     else :
#         print(int(d[2]/2 + d[1]))
import math
def primeFactors(n):
    mx = 1
    while n % 2 == 0:
        mx = 2
        n = n / 2
    for i in range(3,int(math.sqrt(n))+1,2):
        while n % i== 0:
            mx = i
            n = n / i
    if n > 2:
        mx = max(mx, n)

        return mx

def gcd(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

n = int(input())
k = int(input())
a = []

for i in range(n):
    a.append(int(input()))

if(n == 1):
    if(a[0] < k):
        print("Yes")
    else:
        print("No")


if(n == 2):
    if(gcd(a[0], a[1]) <= k ):
        print("Yes")
    else:
        print("No")

num = gcd(a[0], a[1])
for i in range(2, n):
    num = gcd(num, a[i])

num = primeFactors(num) 
if(num <= k):
    print("Yes")
else:
    print("No")



































