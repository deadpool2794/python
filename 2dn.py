# import math

# def modInverse(a, m):
#     m0 = m
#     y = 0
#     x = 1
#     if (m == 1):
#         return 0
#     while (a > 1):
#         q = a // m
#         t = m
#         m = a % m
#         a = t
#         t = y
#         y = x - q * y
#         x = t
#     if (x < 0):
#         x = x + m0
#     return x

# def checkEquality(string):
#     open, close = 0, 0
#     for i in string:
#         if i == "(":
#             open += 1
#         else :
#             close += 1
#     if open == close:
#         return True
#     else:
#         return False

# comb = []

# def check(string):
#     open, close =0, 0
#     for i in string:
#         if i == '(':
#             open += 1
#         else :
#             close += 1
#         if open < close:
#             return False
#     else:
#         return True

# def getTotalPossible(n,string, open ,close):
#     if open + close == n:
#         if open >= close:
#             if check(string):
#                 comb.append(string)
#         return
#     string += "("
#     open += 1
#     getTotalPossible(n, string, open, close)
#     open -= 1
#     string = string[:-1]
#     string += ")"
#     close += 1
#     getTotalPossible(n, string, open, close)


# n = int(input())
# string = ""
# open, close = 0, 0
# getTotalPossible(n,string, open ,close)
# ct = 0
# for i in comb:
#     if checkEquality(i):
#         ct+= 1
# totComb = len(comb)
# print(len(comb))
# gcd = math.gcd(ct, totComb)
# ct /= gcd
# # totComb /= gcd 
# req = ct*totComb
# m = 1000000007
# print(totComb)



# ll binExpo(ll a, ll b){
#     int ans = 1;
#     while(b){
#         if (b&1){
#             ans = (ans *1LL * a) % M;
#         }
#         a = (a * 1LL * a) % M;
#         b >>= 1;
#     }
#     return ans;
# }

M = 1e9+7

def binExpo(a ,b):
    ans = 1
    while b:
        if (b & 1):
            ans = (a * a) % M
        a =(a * a) % M
        b >>= 1
    return ans



cities = int(input())
wc = int(input())
wp = int(input())

print(binExpo(2, 4))
