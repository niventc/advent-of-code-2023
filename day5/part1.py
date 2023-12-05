
# define structure for range map
# parse file
# calculate

# seed-to-soil map: 
# dest_range_start | source_range_start | range_length
# 50               | 98                 | 2
# 52               | 50                 | 48

# 98 -> 50
# 99 -> 51
# 50 -> 52
# 51 -> 53

from typing import Dict, List, Tuple


class RangeMap:

    # source_start, source_end -> dest_start
    values: List[Tuple[int, int, int]] = []

    def __init__(self, input: List[Tuple[int, int ,int]]) -> None:
        self.values = [(value[1], value[1] + value[2], value[0]) for value in input]
        self.values.sort(key=lambda value: value[0])

    def get_dest(self, value: int) -> int:
        match = next((x for x in self.values if value >= x[0] and value < x[1]), None)
        if match is None:
            return value
        
        diff = value - match[0]
        new = match[2] + diff
        # print(f"found {new} from {value} using {match}")
        return new

seeds = []
maps: Dict[str, RangeMap] = {
    "seed-to-soil": None,
    "soil-to-fertilizer": None,
    "fertilizer-to-water": None,
    "water-to-light": None,
    "light-to-temperature": None,
    "temperature-to-humidity": None,
    "humidity-to-location": None
}

with open("input.txt") as file:
    map_name = ""
    map_items = []
    for line in file:
        line = line.rstrip()
        if line.startswith("seeds: "):
            seeds = list(map(lambda x : int(x), line.split(": ")[1].split(" ")))
        elif "map:" in line:
            map_name = line.split(" ")[0]
        elif map_name != "":
            if line != "":
                map_items.append(list(map(lambda x: int(x), line.split(" "))))
            else:
                maps[map_name] = RangeMap(map_items)
                map_name = ""
                map_items = []
    if map_name != "":
        maps[map_name] = RangeMap(map_items)
        map_name = ""
        map_items = []

print(maps)

seed_locations = {}

for seed in seeds:
    location = seed
    print(f"{seed}:")
    for (name, map) in maps.items():
        location = map.get_dest(location)
        print(f"  {name}: {location}")
    seed_locations[seed] = location

print(seed_locations)
print(min(seed_locations.values()))

# 322500873
