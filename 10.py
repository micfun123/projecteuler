#Find the sum of all the primes below two million.

import math
primes = []
def isPrime(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

for i in range(1, 2000000):
    if isPrime(i):
        primes.append(i)

print(sum(primes))