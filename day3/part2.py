
# brute force, look around every cell, buffer number

from typing import List, Set


grid = []
numbers = []
gears: List[Set[int]] = [] # [number_idx]

# generate 2d grid
with open("input.txt") as file:
    # (raw, number, adjacent)
    grid = [[(cell, None) for cell in [*line.rstrip()]] for line in file]

height = len(grid)
width = len(grid[0])

number_idx = 0

# tag numbers
for row_idx in range(height):
    number_buffer = ""
    for col_idx in range(width):
        (value, number) = grid[row_idx][col_idx]

        if value.isnumeric():
            number_buffer += value
            grid[row_idx][col_idx] = (value, number_idx)
        else:
            if number_buffer != "":
                numbers.append(int(number_buffer))
                number_idx += 1
                number_buffer = ""

    if number_buffer != "":
                numbers.append(int(number_buffer))
                number_idx += 1
                number_buffer = ""

gear_idx = 0


def set_cell_adjacent(gear_idx, y, x):
    if x >= 0 and x < width and y >= 0 and y < height:
        (value, number_idx) = grid[y][x]

        if number_idx is not None and gear_idx is not None:
            gears[gear_idx].add(number_idx)

# identify gear adjacent numbers and store per gear
for row_idx in range(height):
    for col_idx in range(width):
        (value, number) = grid[row_idx][col_idx]
        if value == "*":
            gears.append(set())
            # mark adjacent
            set_cell_adjacent(gear_idx, row_idx-1, col_idx-1)
            set_cell_adjacent(gear_idx, row_idx, col_idx-1)
            set_cell_adjacent(gear_idx, row_idx+1, col_idx-1)
            set_cell_adjacent(gear_idx, row_idx-1, col_idx)
            set_cell_adjacent(gear_idx, row_idx+1, col_idx)
            set_cell_adjacent(gear_idx, row_idx-1, col_idx+1)
            set_cell_adjacent(gear_idx, row_idx, col_idx+1)
            set_cell_adjacent(gear_idx, row_idx+1, col_idx+1)

            gear_idx += 1

print(sum(numbers[gear.pop()] * numbers[gear.pop()] for gear in gears if len(gear) == 2))

# 77509019