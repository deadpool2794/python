def countDer(n):
    if n == 1 or n == 2:
        return 1
    a = 1
    b = 1
    for i in range(3, n + 1):
        cur = (i-1)*(a+b)
        a = b
        b = cur
    return b


n = int(input())
for i in range(n):
    print(countDer(int(input())), end = " ")
