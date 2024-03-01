from math import sqrt

#We can see thatis the first triangle number to have over five divisors.
#What is the value of the first triangle number to have over five hundred divisors?


#find first triangle number with over 500 divisors

for i in range(490,100000):
    triangle = i*(i+1)/2
    divisors = 0
    triangle = int(triangle)
    for j in range(1,triangle+1):
        if triangle%j == 0:
            divisors += 1
    if divisors > 500:
        print(triangle)
        break


