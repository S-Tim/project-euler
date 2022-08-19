distinct_powers = set()

for i in range(2, 101):
    for j in range(2, 101):
        distinct_powers.add(i ** j)

print(len(distinct_powers))
