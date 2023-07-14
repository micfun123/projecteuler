#Problem 3
#
#The prime factors of 13195 are 5, 7, 13 and 29.
#
#What is the largest prime factor of the number 600851475143 ?

import math

def compute():
	n = 600851475143
	while True:
		p = smallest_prime_factor(n)
		if p < n:
			n //= p
		else:
			return str(n)


# Returns the smallest factor of n, which is in the range [2, n]. The result is always prime.
def smallest_prime_factor(n):
    assert n >= 2
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return i
    return n  # n itself is prime

print(compute())