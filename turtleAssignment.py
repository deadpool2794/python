from turtle import *
from math import sin, cos, pi

def getVertices(n):
    points = []
    for i in range(1, n + 2):
        x, y = sin((i * 2 * pi) / n) * magnifier, cos((i * 2 * pi) / n) * magnifier
        points.append((x, y))

    return points


def printStar(n):
    points = getVertices(n)

    temp, pos = n, 0
    
    t.penup()
    t.setpos(points[0][0], points[0][1])
    t.pendown()

    while temp:
        temp -= 1
        pos += n // 2
        pos %= n
        t.goto(points[pos][0], points[pos][1])

if __name__ == "__main__":
    t = Turtle()
    n = int(input())
    magnifier = max(100, n * 10)

    if n % 2 == 0 or n < 3:
        print("N is not a valid number")
    else:
        printStar(n)

    t.screen.mainloop()
