def getMaxMin(a, i, k):
    maxi = 0
    mini = 10e9+1
    for j in range(len(a)):
        if j < i or j > i+k-1:
            maxi = max(maxi, a[j])
            mini = min(mini, a[j])
    return maxi , mini

def solution(A, K):
    req = max(A)
    for i in range(len(A) - K + 1):
        maxi , mini= getMaxMin(A, i, K)
        req = min(maxi - mini, req)
    print(req)

arr = [int(x) for x in input().split()]
k = int(input())
solution(arr, k)