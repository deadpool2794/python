# def solution(A):
#     d = {}

#     for i in A:
#         try:
#             d[i] += 1
#         except:
#             d[i] = 1
#     maxi = 0
#     for i in d:
#         if(d[i] == i):
#             maxi = max(i, maxi)
#     print(maxi)

# arr = [int(x) for x in input().split()]

# solution(arr)



# from msilib.schema import ODBCDataSource


# st = input()
# d = {}
# for i in st:
#     try:
#         d[i]+= 1
#     except:
#         d[i] = 1
# ct = 0
# n = len(st)
# arr =list( d.values())
# odd_arr = []
# for i in arr:
#     if i%2 == 1:
#         odd_arr.append(i)

# if n%2 == 0:
#     odd_arr.sort()
#     odd_len = len(odd_arr)/2
#     odd_len = int(odd_len)
#     for i in range(odd_len):
#         ct += odd_arr[i]
# else :
#     odd_arr.sort()
#     odd_arr.pop()
#     odd_len = len(odd_arr)/2
#     odd_len = int(odd_len)
#     for i in range(odd_len):
#         ct += odd_arr[i]

# print(ct) 


# def verify(arr):
#     for i in range(1, len(arr)-1):
#         if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
#             return True
#     return False


# n = int(input())
# arr = [int(i) for i in input().split()]
# res = [-1 for i in range(n)]
# days = 1
# while(verify(arr)):
    
#     for i in range(1, len(arr)-1):
#         if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
#             arr[i] = -1
#             res[i] = days
#     temp = []
#     for i in arr:
#         if i != -1:
#             temp.append(i)
#     arr = temp
#     days += 1
# for i in res:
#     if i == -1:
#         print(0, end = " ")
#     else :
#         print(i, end = " ")

# def calc(i, steps):
#     if(steps == n):
#         return i-1
#     if(i == n):
#         return 1e9
    
#     return min(calc(i+1, steps+i), calc(i+1, steps-i))


# n = int(input())

# steps , cnt, i  = 0, 0, 1
# print(calc(i, steps))
# while(steps != n):
#     if(steps + i <= n) :
#         steps += i
#     else:
#         steps -= i
#     i += 1
#     cnt += 1
# print(cnt)

# input1 = input().split()

# mx, mn = 0, 1e9

# for i in input1:
#     mx = max(mx, len(i))
#     mn = min(mn, len(i))
# print(mx-mn)



# def f(num):
#     if(len(num) == 16):
#         num = int(num)
#         if(num % 90 == 0):
#             print(num, cnt(num, '5'), cnt(num, '0'))
#         return
#     f(num+'0')
    # f(num+'5')

# def cnt(num, dig):
#     num = str(num)
#     res = 0
#     for i in num:
#         if(i == dig):
#             res += 1
        
#     return res

# n = int(input())
# nums = [int(x) for x in input().split()]
# z, n = cnt(nums, '0'), cnt(nums, '5')
# n -= (n%9)
# if(z == 0):
#     print(-1)
# else :
#     b = False
#     if(n):
#         print('5'*n, end = "")
#         b = True
#     print('0'*z) if b else print('0')
        
    
# n, k = map(int, input().split())
# res = 0
# while(n):
#     res += (n%k)
#     n //= k
# print(res)

n, k = int(input()), int(input())
res = 0
while(n):
    res += (n%k)
    n //= k
print(res)   

