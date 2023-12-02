
# target: 12 red cubes, 13 green cubes, and 14 blue cubes

limits = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def check_game(id: str, game: str) -> int:
    sets = game.rstrip().split("; ")
    for set in sets:
        colour_counts = set.rstrip().split(", ")
        for colour_count in colour_counts:
            (count, colour) = colour_count.rstrip().split(" ")

            print(f"{id} - {colour}: {count}")

            if limits[colour] < int(count):
                print(f"{id} unplayable")
                return 0
    return int(id)

with open("input.txt") as file:
    sum = 0

    for line in file:
        (id_str, games) = line.split(": ")
        (game, id) = id_str.split(" ")

        sum += check_game(id, games)

    print(sum)
