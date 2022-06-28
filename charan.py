# def isPalindrome(string):
#     i, j = 0, len(string)-1
#     while(i <=j ):
#         if(string[i] != string[j]):
#             return False
#         i+=1
#         j-=1
#     return True

# def game(cls, input1):
#     palin = ""
#     mx = 0
#     for i in range(len(input1)):
#         for j in range(i+1, len(input1)+1):
#             if(isPalindrome(input1[i:j])):
#                 if mx < len(input1[i:j]):
#                     mx = len(input1[i:j])
#                     palin = input1[i:j]
#     return palin


# def RemoveDuplicates(cls,input1, input2):
#     input1.append(0)
#     res = []
#     for i in range(len(input1)-1):
#         if(input1[i] != input1[i+1]):
#             res.append(input1[i])
#     return res

# def reverseString(cls, input1):
#     string = ""
#     input1 = input1.split()
#     input1 = input1[::-1]
#     for i in range(len(input1)-1):
#         string += input1[i] + " "
#     string += input1[-1]
#     return string

# def anagramCheck(cls, input1, input2):
#     input1 = sorted(input1)
#     input2 = sorted(input2)
#     if(input1 == input2):
#         return "yes"
#     return "no"



n = int(input())
entry = [int(x) for x in input().split()]
exit = [int(x) for x in input().split()]
j = max(exit)
i = n
mat = []
for i in range(n):
    row = [0] * j
    for k in range(j):
        if k >= entry[i]-1 and k < exit[i]-1:
            row[k] = 1
    mat.append(row)

req = 0
for n in range(len(mat[0])):
    sum = 0
    for m in range(len(mat)):
        sum += mat[m][n]
    req = max(req, sum)
print(req)
    