
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

import math

def isPrime(num):
    for i in range(2, int((math.sqrt(num) + 1))):
        if num % i == 0:
            return False
    return True

limit = 10001
primes = [2]
current = 3

while(len(primes) < limit):
    if(isPrime(current)):
        primes.append(current)
    current += 2

print(primes[-1])
