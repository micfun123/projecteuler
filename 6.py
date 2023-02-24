#Sum square difference
#
#Problem 6
#
#The sum of the squares of the first ten natural numbers is, 1^2 + 2^2 + ... + 10^2 = 385
#
#The square of the sum of the first ten natural numbers is, (1 + 2 + ... + 10)^2 = 55^2 = 3025
#
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is
#
#
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sumofsquares(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**2
    return sum

def squareofsum(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum**2

print(squareofsum(100)-sumofsquares(100))
