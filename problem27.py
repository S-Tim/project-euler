import math


def is_prime(n: int) -> bool:
    if n < 0:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


max_consecutive_primes = 0
max_coefficients = (0, 0)

for a in range(-1000, 1001):
    for b in range(-100, 1001):
        current_consecutive_primes = 0
        index = 0
        while is_prime(index * index + a * index + b):
            current_consecutive_primes += 1
            index += 1

        if current_consecutive_primes > max_consecutive_primes:
            max_consecutive_primes = current_consecutive_primes
            max_coefficients = (a, b)
            print('New max coefficients', max_coefficients, 'with product', max_coefficients[0] * max_coefficients[1],
                  'consecutive primes', max_consecutive_primes)

print('Max coefficients', max_coefficients, 'with product', max_coefficients[0] * max_coefficients[1],
      'consecutive primes', max_consecutive_primes)
