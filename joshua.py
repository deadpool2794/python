# def f(ind, k):
#     if (ind == n):
#         return 0
#     if(s[ind] == t[ind]):
#         return 1 + f(ind+1)
#     ans = -1
#     if(k >= abs(s[ind]-t[ind])):
#         ans = max(ans, 1 + f())

    

def length(s):
    return len(s)

class A:
    def __init__(self):
        self.a = 23

def sameSubstring(s, t, K):
    n = length(s)
    ans = 0
    for i in range(n):
        j, temp = i, K
        while(j < n):
            if(s[j] != t[j]):
                absv = abs(ord(s[j]) - ord(t[j]))
                if(temp >= absv):
                    temp -= absv
                else:
                    break
            j += 1
        ans = max(ans, j-i)
    return ans

s, t = "hffk", "larb"
k = 3
print(sameSubstring(s, t, k))
a = A()

print("Hiii")

print("Byeee")