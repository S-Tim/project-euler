from itertools import permutations

perms = permutations('0123456789', 10)
for _ in range(999_999):
    next(perms)
print(''.join(next(perms)))
