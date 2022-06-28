def isPrime(num):
    i = 2
    while(i*i <= num):
        if num%i== 0:
            return False
        i+=1
    return True

arr = [int(i) for i in input().split()]
mn = 1e9
for i in range(len(arr)):
    if arr[i] < mn:
        mn = arr[i]
        mn_ind = i
q = mn
arr.pop(mn_ind)


prod = 1
for i in arr:
    prod *= i
prod += q

if isPrime(prod):
    print(prod)
else :
    print("None")
