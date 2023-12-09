
from typing import List

def get_diffs(sequence: List[int]) -> List[int]:
    diffs = []
    for idx in range(1, len(sequence)):
        diffs.append(sequence[idx] - sequence[idx - 1])
    return diffs


def get_next(sequence: List[int]) -> int:
    print(sequence)
    
    value = sequence[0]
    if all([x == value for x in sequence]):
        return value
    
    return sequence[-1] + get_next(get_diffs(sequence))


with open("input.txt") as file:
    sequences = [list(map(lambda x: int(x), line.rstrip().split(" "))) for line in file.readlines()]

    print(sequences)

    print(sum([get_next(s) for s in sequences]))

# 1637452029