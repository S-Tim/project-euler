def print_spiral():
    for row in number_spiral:
        for n in row:
            print(n, end=' ')
        print('\n')

    print('\n')


width = 1001
center = width // 2
number_spiral = []
for i in range(width):
    row = []
    for j in range(width):
        row.append(0)
    number_spiral.append(row)

current_x = center
current_y = center
number_spiral[center][center] = 1

current_run = 1
current_index = 2

while current_index < width * width:
    # fill right
    for j in range(current_run):
        current_x += 1
        if current_x < width:
            number_spiral[current_y][current_x] = current_index
            current_index += 1
    # fill down
    for j in range(current_run):
        current_y += 1
        if current_y < width and current_x < width:
            number_spiral[current_y][current_x] = current_index
            current_index += 1
    # increment run
    current_run += 1
    # fill left
    for j in range(current_run):
        current_x -= 1
        if current_x >= 0 and current_y < width:
            number_spiral[current_y][current_x] = current_index
            current_index += 1
    # fill up
    for j in range(current_run):
        current_y -= 1
        if current_y >= 0 and current_x >= 0:
            number_spiral[current_y][current_x] = current_index
            current_index += 1
    # increment run
    current_run += 1

s = sum([number_spiral[i][i] for i in range(width)])
s += sum([number_spiral[i][width - i - 1] for i in range(width)])
s -= number_spiral[center][center]
print(s)
