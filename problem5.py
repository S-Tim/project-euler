# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def is_divisible_by_all(num, max):
    for divisor in range(max, 1, -1):
        if num % divisor != 0:
            return False
    return True

num = 25
current = num
while(not is_divisible_by_all(current, num)):
    current += num

print(current)
