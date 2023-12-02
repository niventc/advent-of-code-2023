
# walk in from left and right

# if left is number, store and stop walking
# if right is number, store and stop walking

def check_line(line: str) -> int:
    left_idx = 0
    left = line[left_idx]
    left_found = left.isnumeric()
    
    right_idx = len(line) - 1
    right = line[right_idx]
    right_found = right.isnumeric()

    while True:
        if left_found and right_found:
            return int(f"{left}{right}")

        if not left_found:
            left_idx += 1
            left = line[left_idx]
            left_found = left.isnumeric()

        if not right_found:
            right_idx -= 1
            right = line[right_idx]
            right_found = right.isnumeric()


with open("input.txt") as file:
    sum = 0
    for dirty_line in file:
        line = dirty_line.rstrip()

        sum += check_line(line)
        
    print(sum)