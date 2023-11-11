# def minCost(price):
#     mn = 2e9
#     n, tot = len(price) , 0
#     for i in range(n - 1):
#         tot += abs(price[i] - price[i+1])
#     mn = min(mn, tot)
#     for i in range(n):
#         cur = tot
#         if i != n-1:
#             cur -= abs(price[i]-price[i+1])
#             cur += abs(price[i]//2 - price[i+1])
#         if(i != 0):
#             cur -= abs(price[i]-price[i-1])
#             cur += abs(price[i]//2 - price[i-1])
#         # print(cur)
#         mn = min(mn, cur)        
#     return mn



# price = [int(x) for x in input().split()]
# print(minCost(price))

def minimumcost(data, k):
    n = len(data) // 2
    data = sorted(enumerate(data, 1), key=lambda x: x[1])
    min_cost = float('inf')
    
    for i in range(1, n):
        total_capacity = data[i][1] + data[i + n][1]
        if total_capacity >= k:
            min_cost = min(min_cost, data[i][0] - 1)
    
    return min_cost if min_cost != float('inf') else -1


n = int(input())
data = [int(x) for x in input().split()]
k = int(input())
result = minimumcost(data, k)
print(result)  