
def check_game(id: str, game: str) -> int:
    sets = game.rstrip().split("; ")

    max = {
        "red": 0,
        "blue": 0,
        "green": 0
    }

    for set in sets:
        colour_counts = set.rstrip().split(", ")
        for colour_count in colour_counts:
            (count, colour) = colour_count.rstrip().split(" ")

            print(f"{id} - {colour}: {count}")

            if int(count) > max[colour]:
                max[colour] = int(count)
            
    return max["red"] * max["blue"] * max["green"]

with open("input.txt") as file:
    sum = 0

    for line in file:
        (id_str, games) = line.split(": ")
        (game, id) = id_str.split(" ")

        sum += check_game(id, games)

    print(sum)

# 63307