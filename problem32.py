def is_pandigital(multiplicand: int, multiplier: int, product: int) -> bool:
    digits = [c for c in "123456789"]
    number_string = str(multiplicand) + str(multiplier) + str(product)
    if len(number_string) != len(digits):
        return False
    for digit in digits:
        if digit not in number_string:
            return False
    return True


pandigitals = set()

for i in range(1, 1000):
    if len(str(i)) != len(set([c for c in str(i)])):
        continue
    for j in range(1, 10000):
        result = i * j
        if is_pandigital(i, j, result):
            # print(result)
            pandigitals.add(result)

print(sum(pandigitals))
