# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))
# mx = 0
# for i in range(n):
#     for j in range(i+1, n):
#         for k in range(j+1, n):
#             for l in range(k+1, n):
#                 mx = max(mx, arr[l]-arr[k]+arr[j]-arr[i])
# print(mx)


n = int(input())
arr1, arr2, cnt = [], [], 0
for i in range(n):
    arr1.append(int(input()))

for i in range(n):
    arr2.append(int(input()))


arr1.sort()
arr2.sort()
s1 , s2 = 0, 0

if(n%4 != 0):  
    for i in range(1, n):
        s1 += arr1[i]
    for i in range(1, n):
        s2 += arr2[i]
else:
    for i in range(n):
        s1 += arr1[i]
    for j in range(n):
        s2 += arr2[i]

while(True):
    
    if(s1 < s2):
        n += 1
        s1 += 100
        cnt+= 1
    else:
        break
print(cnt)
    

    




 



