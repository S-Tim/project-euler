# Lattice paths
# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

def lattice_paths(grid_size, row=0, column=0, paths=0, grid_helper={}):
    # if we've been here before, just return the number of paths
    if (row, column) in grid_helper:
        return grid_helper[(row, column)]

    current_paths = 0

    if row == grid_size:
        current_paths = 1
    elif column == grid_size:
        current_paths = paths + \
            lattice_paths(grid_size, row + 1, column, grid_helper=grid_helper)
    else:
        current_paths = paths + lattice_paths(grid_size, row + 1, column, grid_helper=grid_helper) + \
            lattice_paths(grid_size, row, column + 1, grid_helper=grid_helper)

    grid_helper[(row, column)] = current_paths
    return current_paths


print(lattice_paths(20))
