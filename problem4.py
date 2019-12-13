
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(num):
    digits = []
    while(num > 0):
        digits.append(num % 10)
        num //= 10

    reversed = list(digits) 
    reversed.reverse()
    return digits == reversed

def products(max):
    for x in range(max):
        for y in range(max):
            yield x * y

print(max([x * y for x in range(1000) for y in range(1000) if is_palindrome(x * y)]))
