
grid = []
numbers = []

# generate 2d grid
with open("input.txt") as file:
    # (raw, number, adjacent)
    grid = [[(cell, None, None) for cell in [*line.rstrip()]] for line in file]

height = len(grid)
width = len(grid[0])

number_idx = 0

# tag numbers
for row_idx in range(height):
    number_buffer = ""
    for col_idx in range(width):
        (value, number, adjacent) = grid[row_idx][col_idx]

        if value.isnumeric():
            number_buffer += value
            grid[row_idx][col_idx] = (value, number_idx, adjacent)
        else:
            if number_buffer != "":
                numbers.append((int(number_buffer), False))
                number_idx += 1
                number_buffer = ""

    if number_buffer != "":
                numbers.append((int(number_buffer), False))
                number_idx += 1
                number_buffer = ""

[print(f"{row}") for row in grid]


def set_cell_adjacent(y, x):
    if x >= 0 and x < width and y >= 0 and y < height:
        (value, number, adjacent) = grid[y][x]
        grid[y][x] = (value, number, True)

        if number is not None:
            print(y, x, number, len(numbers))
            numbers[number] = (numbers[number][0], True)


# mark tagged numbers that are adjacent to symbols
for row_idx in range(height):
    for col_idx in range(width):
        (value, number, adjacent) = grid[row_idx][col_idx]
        if not value.isnumeric() and value != ".":
            # mark adjacent
            set_cell_adjacent(row_idx-1, col_idx-1)
            set_cell_adjacent(row_idx, col_idx-1)
            set_cell_adjacent(row_idx+1, col_idx-1)
            set_cell_adjacent(row_idx-1, col_idx)
            set_cell_adjacent(row_idx+1, col_idx)
            set_cell_adjacent(row_idx-1, col_idx+1)
            set_cell_adjacent(row_idx, col_idx+1)
            set_cell_adjacent(row_idx+1, col_idx+1)


print(numbers)
print(sum([record[0] for record in numbers if record[1]]))

# 529618