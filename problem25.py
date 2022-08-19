def fibonacci(length: int) -> (int, int):
    index = 2
    a = 1
    b = 1

    while len(str(a)) < length:
        temp = a + b
        b = a
        a = temp
        index += 1

    return index, a


# for i in range(1, 5):
#     print(fibonacci(i))

print(fibonacci(1000))
