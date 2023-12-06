
time = None
distance = None

with open("input.txt") as file:
    lines = file.readlines()
    time = int("".join(lines[0].rstrip().split()[1:]))
    target_distance = int("".join(lines[1].rstrip().split()[1:]))

    print(time)
    print(distance)

winning_attempts = 0

for attempt_id in range(1, time + 1):
    speed = attempt_id
    moving = time - attempt_id
    distance = moving * speed
    print(f"{distance} - {target_distance}")

    if distance > target_distance:
        winning_attempts += 1

print(f"{winning_attempts}")

# 32607562