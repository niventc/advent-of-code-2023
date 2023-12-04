
sum = 0

with open("input.txt") as file:
    for line in file:
        (id, game) = line.split(": ")
        (ours_str, winning_str) = game.rstrip().split(" | ")
        ours = set(x for x in ours_str.rstrip().split(" ") if x)
        winning = set(x for x in winning_str.rstrip().split(" ") if x)

        intersection = list(ours & winning)
        winning_count = len(intersection)

        if winning_count == 1:
            sum += 1
        elif winning_count > 1:
            sum += pow(2, (winning_count - 1))

print(sum)
        
# 18653
