target = 200
coins = [1, 2, 5, 10, 20, 50, 100, 200]
solutions = [0] * (target + 1)
solutions[0] = 1

for coin in coins:
    for i in range(coin, len(solutions)):
        solutions[i] += solutions[i - coin]

print(solutions[target])


solutions = 0
for a in range(0, target + 1, 200):
    for b in range(a, target + 1, 100):
        for c in range(b, target + 1, 50):
            for d in range(c, target + 1, 20):
                for e in range(d, target + 1, 10):
                    for f in range(e, target + 1, 5):
                        for g in range(f, target + 1, 2):
                            solutions += 1

print(solutions)
