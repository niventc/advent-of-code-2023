
lines = []
distances = []

with open("input.txt") as file:
    lines = file.readlines()
    times = list(map(lambda x: int(x), lines[0].rstrip().split()[1:]))
    distances = list(map(lambda x: int(x), lines[1].rstrip().split()[1:]))

    print(times)
    print(distances)

winning_product = 1

for game_idx in range(len(times)):
    winning_attempts = 0

    for attempt_id in range(1, times[game_idx] + 1):
        speed = attempt_id
        moving = times[game_idx] - attempt_id
        distance = moving * speed
        print(f"{distance} - {distances[game_idx]}")

        if distance > distances[game_idx]:
            winning_attempts += 1

    print(f"{winning_attempts}")
    winning_product *= winning_attempts

print(winning_product)

# 503424