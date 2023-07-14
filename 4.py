#Problem 4#

#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.#

#Find the largest palindrome made from the product of two 3-digit numbers.
biggest = 0

def isPalindrome(n):
    return str(n) == str(n)[::-1]

#find the biggest palindrome made from the product of two 3-digit numbers
for i in range(100, 1000):
    for j in range(100, 1000):
        if isPalindrome(i*j) and i*j > biggest:
            biggest = i*j

print(biggest)