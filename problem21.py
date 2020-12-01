import math


def sum_of_divisors(number: int) -> int:
    s = 1
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            s += i

            counterpart = number // i
            if counterpart != i:
                s += counterpart

    return s


def is_amicable(a: int) -> bool:
    b = sum_of_divisors(a)
    return sum_of_divisors(a) == b and sum_of_divisors(b) == a and a != b


amicable_sum = 0
for i in range(2, 10000):
    if is_amicable(i):
        print(i)
        amicable_sum += i

print('Sum:', amicable_sum)
