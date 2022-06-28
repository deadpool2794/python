# print('hello world')
# test_string = "happybirthday"
# x = [print(i) for i in test_string if i not in "aeiou"]

def Sum(a,b):
    try:
        c = ((a+b) / (a-b))
    except ZeroDivisionError:
         print("Error")
   
    else:
        print(c)

# Sum(3,3)
input()
a=map(int,input().split())
m=min(a)
print(-1,'1\n'+str(a.index(m)+1))[2*m<sum(a)]