def reciprocal_count(number: int) -> int:
    remainders = []
    current_remainder = 1
    length = 0

    while current_remainder < number:
        current_remainder *= 10
    current_remainder = current_remainder % number

    while current_remainder not in remainders and current_remainder != 0:
        remainders.append(current_remainder)

        while current_remainder < number:
            current_remainder *= 10
            length += 1

        current_remainder = current_remainder % number

        if current_remainder == 0:
            return -1

    return length


# for i in range(2, 11):
#     print(i, reciprocal_count(i))
print(reciprocal_count(2))

max_reciprocal = 0
max_digit = 0
for i in range(2, 1000):
    value = reciprocal_count(i)
    if value > max_reciprocal:
        max_reciprocal = value
        max_digit = i
        print(max_digit, max_reciprocal)

print(max_digit, max_reciprocal)
