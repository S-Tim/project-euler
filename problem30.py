def is_fifth_power_of_digits(number: int) -> bool:
    return sum([int(digit) ** 5 for digit in str(number)]) == number


numbers = [i for i in range(2, 10000000) if is_fifth_power_of_digits(i)]
print(numbers, sum(numbers))
