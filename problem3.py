import math

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

def factorize(num):
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return [i] + factorize(num // i)
    return [num]

for num in range(2, 100):
    print(num, factorize(num))

# print(factorize(600851475143))
# print(max(factorize(600851475143)))
