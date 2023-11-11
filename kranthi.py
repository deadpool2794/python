# def lexicographicallySmallest(input1, input2):
#     input2 = sorted(input2)
#     for i in input2:
#         print(i , end="")

# input1 =int( input()[0])

def f(x):
    k, st = 0, []
    while(x < n):
        if m[x] == '(':
            # print("HII")
            st.append('(')
            print(x, m[x], st, m[x] == '(', "OPEN", len(st))
        else:
            if(len(st) != 0):
                print(len(st), st[len(st)-1])

            if(len(st) > 0 and st[len(st)-1] == '('):
                st.pop()
            else:
                return k
        k += 1
        x += 1

        return k


n = int(input())
m = input()
ans = 0
for i in range(n):
    # print("HII")
    ans = max(ans, f(i))

print(ans)
