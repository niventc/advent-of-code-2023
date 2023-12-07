
from collections import Counter
from functools import cmp_to_key
from typing import List, Tuple

values = {
    "A": 13, 
    "K": 12, 
    "Q": 11,
    "J": 1,
    "T": 10
}

def parse_value(value: str) -> int:
    if value.isnumeric():
        return int(value)
    
    return values[value]

def score_hand(cards: str) -> int:
    counts = Counter(card for card in cards if card != 'J')

    # add joker values to max
    jokers = len([card for card in cards if card == 'J'])
    if jokers:
        if jokers == 5:
            return 7
        else:
            counts.update({counts.most_common(1)[0][0]: jokers})

    if len(counts) == 1:
        return 7
    elif len(counts) == 2:
        if max(counts.values()) == 4:
            return 6
        else:
            return 5
    elif len(counts) == 3:
        if max(counts.values()) == 3:
            return 4
        else:
            return 3
    elif len(counts) == 4:
        return 2
    else:
        return 1


# List[str] = raw, List[int] = number, score, bid
def parse_hand(line: str) -> Tuple[List[str], List[int], int]:
    (cards, bid) = line.split()
    card_values = [parse_value(card) for card in cards]
    return (cards, card_values, score_hand(cards), int(bid))

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


    sum = 0
    for idx in range(len(hands)):
        sum += hands[idx][3] * (idx + 1)
        print(hands[idx])

    print(sum)

# 246436046