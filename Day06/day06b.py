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


def check_for_loop(location, array):
    x, y, direction = location

    array[next_step(x, y, direction)[1]][next_step(x, y, direction)[0]] = '#'
    direction = (direction + 1) % 4
    x, y = next_step(x, y, direction)

    visited_locations = []

    while True:
        while get_next_step(x, y, direction, array) != '#':
            if (x, y, direction) in visited_locations: return True
            else: visited_locations.append((x, y, direction))
            x, y = next_step(x, y, direction)
            if off_map(x, y, direction, array): return False
        direction = (direction + 1) % 4


def get_guard_location(array):
    for y in range(len(array) - 1):
        for x, column in enumerate(array[y]):
            if column == "^":
                return x, y
    return -1, -1


if __name__ == "__main__":
    array = get_input(f"src/inputA/{input_path}.txt")
    num_loops = get_num_loops(array)
    print(num_loops)


