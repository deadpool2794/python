# string s; cin >> s;
s = input()
lo = 0
hi = pow(10, pow(10, 5))
ind = 1
arr = []
for i in s:
    m = lo/2+hi/2
    arr.append([m, ind])
    ind+=1
    if(i == 'l'):
        hi = m
    else:
        lo = m

arr.sort()
for i in arr:
    print(i[1])