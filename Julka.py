for _ in range(10):
    tot = int(input())
    rem = int(input())
    tot -= rem
    tot //= 2
    print(tot+rem)
    print(tot)