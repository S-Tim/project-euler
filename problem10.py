# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

import math

def isPrime(num):
    for i in range(2, int((math.sqrt(num) + 1))):
        if num % i == 0:
            return False
    return True

limit = 2000000
primes = [2]
current = 3

while(current < limit):
    if(isPrime(current)):
        primes.append(current)
    current += 2

print(sum(primes))
