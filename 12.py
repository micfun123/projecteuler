#We can see thatis the first triangle number to have over five divisors.
#What is the value of the first triangle number to have over five hundred divisors?


#find first triangle number with over 500 divisors

#for i in range(490,100000):
#    triangle = i*(i+1)/2
#    divisors = 0
#    triangle = int(triangle)
#    for j in range(1,triangle+1):
#        if triangle%j == 0:
#            divisors += 1
#    if divisors > 500:
#        print(triangle)
#        break


import math

def count_divisors(n):
    count = 0
    sqrt_n = int(math.sqrt(n))
    for i in range(1, sqrt_n + 1):
        if n % i == 0:
            count += 2
    if sqrt_n * sqrt_n == n:
        count -= 1  # If n is a perfect square, we counted its square root twice
    return count

divisors_needed = 500
triangle = 1
increment = 2
while True:
    if count_divisors(triangle) > divisors_needed:
        print(triangle)
        break
    triangle += increment
    increment += 1
