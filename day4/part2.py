
cards = [1] * 199
idx = 0

with open("input.txt") as file:
    for line in file:
        (id, game) = line.split(": ")
        (ours_str, winning_str) = game.rstrip().split(" | ")
        ours = set(x for x in ours_str.rstrip().split(" ") if x)
        winning = set(x for x in winning_str.rstrip().split(" ") if x)

        intersection = list(ours & winning)
        winning_count = len(intersection)

        for c in range(cards[idx]):
            for x in range(1, winning_count + 1):
                cards[idx+x] += 1

        idx += 1

print(sum(cards))
        



