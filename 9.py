a = 1
b = 1
c = 1

for a in range(100,500):
    for b in range(100,500):
        for c in range(100,500):
            if a + b + c == 1000:
                if a**2 + b**2 == c**2:
                    print(a*b*c)
                    print(a,b,c)
                    break
                    