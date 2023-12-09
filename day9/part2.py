
from itertools import pairwise
from typing import List

def get_diffs(sequence: List[int]) -> List[int]:
    return [x[1] - x[0] for x in pairwise(sequence)]


def get_next(sequence: List[int]) -> int:
    print(sequence)
    
    value = sequence[0]
    if all([x == value for x in sequence]):
        return value
    
    return sequence[0] - get_next(get_diffs(sequence))


with open("input.txt") as file:
    sequences = [list(map(lambda x: int(x), line.rstrip().split(" "))) for line in file.readlines()]

    print(sequences)

    print(sum([get_next(s) for s in sequences]))

# 908