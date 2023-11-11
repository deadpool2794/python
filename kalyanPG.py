# n = int(input())
# spaces = ' '
# start = ''
# k, l = 1, 4*n-5
# for i in range(n-1):
#     print(start, end = '')
#     print(k, end = '')
#     print(spaces*l, end = '')
#     print(k)
#     start = start + "  "
#     k += 1
#     l -= 4
# print(start, end = "")
# print(n)
# k -= 1 
# l = 3
# start = start[:len(start)-2]
# for i in range(n-1):
#     print(start, end = '')
#     print(k, end = '')
#     print(spaces*l, end = '')
#     print(k)
#     l += 4    
#     start = start[:len(start)-2]
#     k -= 1


# n = int(input())
# spaces = ' '
# start = ''
# k, l = 1, 
# for i in range(n-1):
#     print(start, end = '')
#     print(k, end = '')
#     print(spaces*l, end = '')
#     print(k)
#     start = start + " " + " "
#     k += 1
#     l -= 4
# print(start, end = '')
# print(n)
# k-= 1 
# l = 3
# start = start[:len(start)-1]
# for i in range(n-1):
#     print(start, end = '')
#     print(k, end = '')
#     print(spaces*l, end = '')
#     print(k)
#     start = start[:len(start)-1]
#     k-=1
#     l += 2  

# a, b = input(), input()

# n = len(a)
# mx, mn = 0, 0
# for i in range(n):
#     if a[i] == '?' and b[i] == '?':
#         mx += 1
#     elif a[i] == '?' or b[i] == '?':
#         mx += 1
#     elif a[i] != b[i]:
#         mx += 1
#         mn += 1
# print(mn, mx)


# s = input()
# n = len(s)
# last = s[len(s)-1]
# if(last.isdigit()):
#     last = ord(last)-ord('0')
#     for j in range(10):
#         if(n+1 == (last*10)+j):
#             print(j-2)
#             break
#     else:
#         print(-1)
# else:
#     if(n >= 10):
#         print(-1)
#     else:
#         print(n)


# n = int(input())
# arr = [int(x) for x in input().split()]
# arr.sort()
# i, j, ans = 0, n-1, 0

# while(i < j):
#     ans += arr[j]-arr[i]
#     i += 1
#     j -= 1

# print(ans)


n = int(input())
arr = [int(x) for x in input().split()]
ans, s = 0, sum(arr)
for i in range(1,n-1):
    mn1, mx1, mn2, mx2 = min(arr[:i]), max(arr[:i]), min(arr[i:]), max(arr[i:])
    ans = max(ans,(mx2-mn2)+ (mx1-mn1))
print(ans)
