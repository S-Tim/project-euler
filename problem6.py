# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(num):
    total = 0
    for i in range(num + 1):
        total += i * i
    
    return total

def square_of_sum(num):
    total = sum(range(num + 1))
    return total * total

limit = 100

print(sum_of_squares(limit))
print(square_of_sum(limit))
print(square_of_sum(limit) - sum_of_squares(limit))
