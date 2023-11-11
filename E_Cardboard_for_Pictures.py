from math import sqrt
def sq(arr):
    res = 0
    for i in arr:
        res += i*i
    return res
 
t = int(input())
while(t):
    t -= 1
    n, c_ = map(int, input().split())
    arr = [int(x) for x in input().split()]
    a = 4*n
    b = 4*sum(arr)
    c = sq(arr) - c_
    r1, r2 = ((-1*b)+sqrt((b**2)-(4*a*c)))/(2*a), ((-1*b)-sqrt((b**2)-(4*a*c)))/(2*a)
    print(int(r1)) if r1 > 0 else print(int(r2))