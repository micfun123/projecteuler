#Problem 5
#
#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def isDivisible(n):
    for i in range(1, 21):
        if n % i != 0:
            return False
    return True

sorting = True
currentnum = 1
while sorting:
    if isDivisible(currentnum):
        sorting = False
    else:
        currentnum += 1
    print(currentnum)