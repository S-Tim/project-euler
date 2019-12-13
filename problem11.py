# In the 20×20 grid below, four numbers along a diagonal line have been marked in red.
# The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally) in the 20×20 grid?

grid = []

with open('problem11.txt', 'r') as grid_txt:
    for line in grid_txt.readlines():
        grid.append([int(num) for num in line.split(' ')])

max_product = 0
adjacent_nums = 4

rows = len(grid)
columns = len(grid[0])

for i in range(rows):
    for j in range(columns):
        # down
        if i <= rows - adjacent_nums:
            product = 1
            for factor in range(adjacent_nums):
                product *= grid[i + factor][j]
            max_product = max(max_product, product)

        # right
        if j <= columns - adjacent_nums:
            product = 1
            for factor in range(adjacent_nums):
                product *= grid[i][j + factor]
            max_product = max(max_product, product)

        # diagonal right
        if i <= rows - adjacent_nums and j <= columns - adjacent_nums:
            product = 1
            for factor in range(adjacent_nums):
                product *= grid[i + factor][j + factor]
            max_product = max(max_product, product)

        # diagonal left
        if i <= rows - adjacent_nums and j >= adjacent_nums - 1:
            product = 1
            for factor in range(adjacent_nums):
                product *= grid[i + factor][j - factor]
            max_product = max(max_product, product)

print(max_product)
