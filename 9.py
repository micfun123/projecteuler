import math
tosolve = 1000

for a in range(1, tosolve):
    for b in range(a+1, tosolve):
        c = math.sqrt(a**2 + b**2)
        if a + b + c == tosolve:
            print(a*b*c)
            print(a, b, c)
            break