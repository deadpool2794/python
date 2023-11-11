import fractions
import sys

print(fractions.__file__)
print(sys.path)

x, y, n = [int(i) for i in input().split()]

ans = fractions.Fraction(x,y).limit_denominator(n)

