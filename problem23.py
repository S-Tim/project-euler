import math

from typing import List


def is_abundant(number: int) -> bool:
    sum_of_divisors = 1
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            sum_of_divisors += i
            if number / i != i:
                sum_of_divisors += number / i

    return sum_of_divisors > number


def is_sum_of_abundants(number: int, abundants: List[int]) -> bool:
    for x in abundants:
        for y in abundants:
            s = x + y
            if s == number:
                return True
            elif s > number:
                break
    return False


print('Calculating abundant numbers...')
abundant_numbers = []
for i in range(1, 28124):
    if is_abundant(i):
        abundant_numbers.append(i)

print('Finding non abundant sum...')
sum_of_non_abundants = 0
for i in range(1, 28124):
    if i % 500 == 0:
        print('Currently at:', i, 'with sum:', sum_of_non_abundants)
    if not is_sum_of_abundants(i, abundant_numbers):
        # print(i)
        sum_of_non_abundants += i

print(sum_of_non_abundants)
