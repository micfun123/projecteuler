#Problem 7
#
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
#What is the 10 001st prime number?
primes = []
i = 0
while len(primes) < 10002:
    i += 1
    print(i)
    isprime = True
    for j in range(2, i):
        if i % j == 0:
            isprime = False
    if isprime:
        primes.append(i)
        
    