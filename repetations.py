string = input()
n = len(string)
count, maxCount = 0, 1

for i in range(n-1):
    if string[i] == string[i+1]:
        count += 1
    else:
        maxCount = max(count+1, maxCount)
        count = 0
print(max(maxCount, count+1))

