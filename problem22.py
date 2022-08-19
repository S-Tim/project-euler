def name_score(name: str) -> int:
    return sum([ord(c) - ord('A') + 1 for c in name])


if __name__ == '__main__':
    with open('names.txt', 'r') as name_file:
        total_score = 0
        names = name_file.read().split(',')
        names = list(map(lambda n: n[1:-1], names))
        names.sort()
        for index, name in enumerate(names):
            total_score += name_score(name) * (index + 1)

        print(total_score)
