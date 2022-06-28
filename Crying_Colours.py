

def swapRedGreen(count):
    while True:
        if red[1] == 0 or green[0]==0:
            return count
        red[0] += 1
        red[1] -=1
        green[1] += 1
        green[0] -= 1
        count += 1
    

def swapRedBlue(count):
    while True:
        if red[2] == 0 or blue[0] == 0:
            return count
        red[0] += 1
        red[2] -= 1
        blue[0] -= 1
        blue[2] += 1
        count += 1
    

def swapGreenBlue(count):
    while True:
        if green[2] == 0 or blue[1] == 0:
            return count
        green[1] += 1
        green[2] -= 1
        blue[2] += 1
        blue [1] -= 1
        count += 1
    


tc = int(input())
for i in range(tc):
    n = int(input())
    count = 0
    red = [int(x) for x in input().split()]
    green = [int(x) for x in input().split()]
    blue = [int(x) for x in input().split()]
    count = swapRedGreen(count)
    count = swapRedBlue(count)
    count = swapGreenBlue(count)
    print(count)