s = input()
d = {}
for i in s:
    try:
        d[i] += 1
    except:
        d[i] = 1
oddCount = 0
for i in d.values():
    if i % 2 == 1:
        oddCount += 1
if oddCount >1:
    print("NO SOLUTION")
else:
    arr = list(s)
    i, j = 0, len(arr) -1
    if len(s) % 2 == 0:
        while i< j:
            for key in d:
                if d[key] != 0:
                    arr[i], arr[j] = key, key
                    d[key] -= 2
                    i += 1
                    j -= 1
    else:
        while i < j:
            for key in d:
                if d[key] > 1:
                    arr[i], arr[j] = key, key
                    d[key] -= 2
                    i += 1
                    j -= 1
        for index in d:
            if d[index] == 1:
                arr[i] =index
    for i in arr:
            print(i, end = "")
            
        
        

