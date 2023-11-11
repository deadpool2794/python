n = int(input())
if n%2 == 0:
    print("n is even", end = ' ')
    if n >= 0 and n <= 10:
        print("and lies between 0 and 10")
    elif n >= 12 and n <= 20:
        print("and lies between 12 and 20")
    else :
        print("and is greater than 20")
else:
    print("n is odd", end = ' ')
    if n >= 1 and n <= 9:
        print("and lies between 1 and 9")
    elif n >= 11 and n <= 19:
        print("and lies between 11 and 19")
    else :
        print("and is greater than 19")

    