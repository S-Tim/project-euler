# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2

# For example, 32 + 42 = 9 + 16 = 25 = 52.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def is_triplet(a, b, c):
    return a*a + b*b == c*c

for c in range(1000, 0, -1):
    for b in range(min(c-1, 1000-c), 0, -1):
        a = 1000 - c - b

        if a > b:
            break
        elif is_triplet(a, b, c):
            print(a, b, c, a*b*c)
