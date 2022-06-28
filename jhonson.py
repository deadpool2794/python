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


def verify(arr):
    for i in range(1, len(arr)-1):
        if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            return True
    return False


n = int(input())
arr = [int(i) for i in input().split()]
res = [-1 for i in range(n)]
days = 1
while(verify(arr)):
    
    for i in range(1, len(arr)-1):
        if arr[i] < arr[i-1] and arr[i] < arr[i+1]:
            arr[i] = -1
            res[i] = days
    temp = []
    for i in arr:
        if i != -1:
            temp.append(i)
    arr = temp
    days += 1
for i in res:
    if i == -1:
        print(0, end = " ")
    else :
        print(i, end = " ")
