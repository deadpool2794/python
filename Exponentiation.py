n = int(input())
m = 1e9+7

for _ in range(n):
    a, b = map(int, input().split())
    pow = 1
    for i in range(b):
        pow *= a
        pow %= m
    print(int(pow))