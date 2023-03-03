a = 1
b = 1
c = 1

for i in range(100,500):
    for j in range(100,500):
        for k in range(100,500):
            if i + j + k == 1000:
                if i**2 + j**2 == k**2:
                    a = i
                    b = j
                    c = k
print(a*b*c)
print(a)
print(b)
print(c)

                    