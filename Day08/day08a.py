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
            antis = get_antinodes(combination[0], combination[1])
            for antinode in antis:
                if 0<=antinode[1]<=width and 0<=antinode[0]<=height: antinode_locations.add(antinode)
    return len(antinode_locations)

def get_antinodes(ant1, ant2):
    d_x = ant1[0] - ant2[0]
    d_y = ant1[1] - ant2[1]
    anti1 = (ant1[0] + d_x, ant1[1] + d_y)
    anti2 = (ant2[0] - d_x, ant2[1] - d_y)
    return anti1, anti2


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