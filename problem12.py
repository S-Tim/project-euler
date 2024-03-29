# The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
# Let us list the factors of the first seven triangle numbers:
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28
# We can see that 28 is the first triangle number to have over five divisors.
# What is the value of the first triangle number to have over five hundred divisors?

import math

def triangle_num(n):
    return int(n/2 * (n+1))

def number_of_divisors(num):
    divisors = set()
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.add(i)
            divisors.add(num // i)
    return len(divisors)

current = 1
while(number_of_divisors(triangle_num(current)) < 500):
    current += 1

print(triangle_num(current))
