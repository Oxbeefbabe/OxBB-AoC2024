import copy

EXAMPLE = False
input_path = "example" if EXAMPLE else "input"

move = {0:[0, -1],
        1:[1, 0],
        2:[0, 1],
        3:[-1, 0]}


def get_input(path):
    input_array = []
    with open(path, "r") as file:
        for line in file:
            input_array.append([c for c in line.strip()])
    return input_array

def off_map(x, y, direction, array):
    if direction == 0:
        return y == 0
    elif direction == 1:
        return x == len(array[0]) - 1
    elif direction == 2:
        return y == len(array) - 1
    else:
        return x == 0

def get_next_step(x, y, direction, array):
    return array[y + move[direction][1]][x + move[direction][0]]

def next_step(x, y, direction):
    return x + move[direction][0], y + move[direction][1]

def get_unique_positions(array):
    x, y = get_guard_location(array)
    direction = 0
    positions = [(x, y, direction)]
    while True:
        if off_map(x, y, direction, array): return positions
        if get_next_step(x, y, direction, array) == '#':
            direction = (direction + 1) % 4
        else: x, y = next_step(x, y, direction)
        if (x, y, direction) not in positions: positions.append((x, y, direction))

def get_num_loops(array):
    x, y = get_guard_location(array)
    loops = 0
    direction = 0
    while True:
        while get_next_step(x, y, direction, array) != '#':
            if check_for_loop((x, y, direction), copy.deepcopy(array)): loops += 1
            x, y = next_step(x, y, direction)
            if off_map(x, y, direction, array): return loops
        direction = (direction + 1) % 4

def get_num_loops_v2(array):
    positions = get_unique_positions(array)
    loops = 0
    blocker_locations = []
    for position in positions:
        blocker_location, loop = check_for_loop(position, copy.deepcopy(array))
        if loop:
            loops += 1
            blocker_locations.append(blocker_location)
    return loops, blocker_locations

def get_num_loops_v3(array):
    # Good god this is inefficient, but I can't see where my other attempts were finding extra loops
    num_of_spaces = len(array) * len(array[0])

    sx, sy = get_guard_location(array)
    blocker_locations = set()
    index = 0
    for y, row in enumerate(array):
        for x, column in enumerate(row):
            index += 1
            print(f"Checking location {index}/{num_of_spaces}")
            if column not in "#^":
                area = copy.deepcopy(array)
                area[y][x] = '#'
                loop = check_for_loop_v2(sx, sy, area)
                if loop: blocker_locations.add((x, y))

    return len(blocker_locations)

def check_for_loop(location, array):
    x, y, direction = location
    if off_map(x, y, direction, array): return None, False
    blocker_location = next_step(x, y, direction)
    array[blocker_location[1]][blocker_location[0]] = '#'
    # direction = (direction + 1) % 4
    # x, y = next_step(x, y, direction)

    visited_locations = []

    while True:
        if off_map(x, y, direction, array): return None, False
        if get_next_step(x, y, direction, array) == '#':
            direction = (direction + 1) % 4
        else: x, y = next_step(x, y, direction)
        if (x, y, direction) in visited_locations: return blocker_location, True
        else: visited_locations.append((x, y, direction))

def check_for_loop_v2(x, y, area):
    direction = 0
    visited_locations = []
    while True:
        if off_map(x, y, direction, area): return False
        if get_next_step(x, y, direction, area) == '#':
            direction = (direction + 1) % 4
        else: x, y = next_step(x, y, direction)
        if (x, y, direction) in visited_locations: return True
        else: visited_locations.append((x, y, direction))

def get_guard_location(array):
    for y in range(len(array)):
        for x, column in enumerate(array[y]):
            if column == "^":
                return x, y
    return -1, -1


if __name__ == "__main__":
    array = get_input(f"src/inputA/{input_path}.txt")
    loops = get_num_loops_v3(array)
    print(loops)


