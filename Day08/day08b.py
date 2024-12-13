import math
from itertools import combinations

EXAMPLE = False
input_path = "example" if EXAMPLE else "input"


def get_input(path):
    ant_map = []
    with open(path, "r") as file:
        for line in file:
            ant_map.append(line.strip())
    return ant_map

def get_num_antinodes(ant_map):
    antenna_locations = get_antenna_locations(ant_map)
    antinode_locations = set()
    width = len(ant_map[0]) - 1
    height = len(ant_map) - 1
    for frequency in antenna_locations:
        antenna_combinations = combinations(antenna_locations[frequency], 2)
        for combination in antenna_combinations:
            antis = get_antinodes(combination[0], combination[1], width, height)
            for antinode in antis:
                if 0<=antinode[0]<=width and 0<=antinode[1]<=height: antinode_locations.add(antinode)
    return len(antinode_locations)

def get_antinodes(ant1, ant2, width, height):
    d_x = ant1[0] - ant2[0]
    d_y = ant1[1] - ant2[1]
    antinodes = []

    d_x, d_y = short(d_x, d_y)

    x, y = ant1
    while 0<=x<=width and 0<=y<=height:
        x -= d_x
        y -= d_y
        antinodes.append((x, y))

    x, y = ant2
    while 0<=x<=width and 0<=y<=height:
        x += d_x
        y += d_y
        antinodes.append((x, y))

    return antinodes

def short(d_x, d_y):
    if d_x == 0: return 0, 1
    if d_y == 0: return 1, 0
    gcd = math.gcd(d_x, d_y)
    return d_x / gcd, d_y / gcd


def get_antenna_locations(ant_map):
    antenna_locations = {}
    for y, row in enumerate(ant_map):
        for x, column in enumerate(row):
            if column != '.':
                if column not in antenna_locations:
                    antenna_locations[column] = [(x, y)]
                else:
                    antenna_locations[column] = antenna_locations[column] + [(x, y)]
    return antenna_locations


if __name__ == "__main__":
    antenna_map = get_input(f"src/inputA/{input_path}.txt")
    print(get_num_antinodes(antenna_map))