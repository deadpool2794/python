# n = int(input())
# space, star = ' ', '*'
# print(star)
# j, f = 1, 1
# for i in range(1, 2*n-2):
#     if(i >= n):
#         if(f == 1):
#             j -= 2
#             f = 2
#         j -= 2
#         print(star, end = '')
#         print(space*(j), end = '')
#         print(star)
#     else:
#         print(star, end = '')
#         print(space*(j), end = '')
#         print(star)
#         j += 2
# print(star)

# s = input()
# ans, noans = 0, False
# ans2 = ''
# stack = []
# for i in s:
#     if(ord(i) < 97):
#         stack.append(i)
#     else:
#         if(len(stack) > 0 and ord(stack[len(stack)-1]) - ord(i) == -32):
#             stack.pop()
#         else:
#             noans = True
#             ans2 = i
#             break
# if(noans):
#     print(ans2)
# elif len(stack) > 0:
#     print(stack[len(stack)-1])
# else :
#     print(len(s)//2)





# arr = [int(x) for x in input().split(',')]
# arr = set(arr)
# arr = list(arr)
# if(len(arr) == 1):
#     print("No Gifts Available")
# else:
#     arr.sort()
#     print(arr[len(arr)-2])


# s, cnt = input(), 1
# for i in range(0, len(s)-1):
#     if(s[i] == s[i+1]):
#         cnt+=1
#     else:
#         print("({}:{})".format(s[i], cnt), end = " ")
#         cnt = 1


# print("({}:{})".format(s[len(s)-1], cnt), end = "")

# word1 = sorted(list(input().lower()))
# word2 = sorted(list(input().lower()))
# dic1, dic2 = {}, {}
# for i in range(97, 123):
#     dic1[chr(i)] = dic2[chr(i)] = 0
# for i in word1:
#     dic1[i] += 1
# for i in word2:
#     dic2[i] += 1

# if(word1 == word2):
#     print(len(word1))
# else:
#     ans = ""
#     for i in word1:
#         if i not in word2:
#             ans += i
#     for i in word2:
#         if i not in word1:
#             ans += i
   
#     ans = sorted(list(ans))
#     for i in ans:
#         print(i, end = '')

a, b = int(input()), int(input())
if(a > b):
    print("Provide valid input")
else:
    primes = []
    while(a <= b):
        for i in range(2, a):
            if a%i == 0:
                break
        else:
            primes.append(a)
        a+=1
    print(*primes)


    






    

































