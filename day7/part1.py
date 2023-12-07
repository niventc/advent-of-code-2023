
from collections import Counter
from functools import cmp_to_key
from typing import List, Tuple

values = {
    "A": 14, 
    "K": 13, 
    "Q": 12,
    "J": 11,
    "T": 10
}

def parse_value(value: str) -> int:
    if value.isnumeric():
        return int(value)
    
    return values[value]


# List[str] = raw, List[int] = number, score, bid
def parse_hand(line: str) -> Tuple[List[str], List[int], int]:
    (cards, bid) = line.split()
    card_values = [parse_value(card) for card in cards]

    counts = Counter(cards)
    score = 0

    if len(counts) == 1:
        score = 7
    elif len(counts) == 2:
        if max(counts.values()) == 4:
            score = 6
        else:
            score = 5
    elif len(counts) == 3:
        if max(counts.values()) == 3:
            score = 4
        else:
            score = 3
    elif len(counts) == 4:
        score = 2
    else:
        score = 1

    return (cards, card_values, score, int(bid))

def compare(left, right) -> int:
    if left[2] > right[2]:
        return 1
    elif left[2] < right[2]:
        return -1
    
    for idx in range(len(left[1])):
        if left[1][idx] > right[1][idx]:
            return 1
        elif left[1][idx] < right[1][idx]:
            return -1


with open("input.txt") as file:
    hands = list(map(parse_hand, file.readlines()))

    hands.sort(key=cmp_to_key(compare))

    print(hands)

    sum = 0
    for idx in range(len(hands)):
        sum += hands[idx][3] * (idx + 1)

    print(sum)

# 248396258