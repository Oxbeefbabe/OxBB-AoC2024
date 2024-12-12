EXAMPLE = False
input_path = "example" if EXAMPLE else "input"


def get_input(path):
    input_array = []
    with open(path, "r") as file:
        for line in file:
            input_array.append([c for c in line.strip()])
    return input_array

def get_unique_locations(array):
    x, y = get_guard_location(array)
    unique_locations = 0
    direction = 1
    while True:
        # ^
        if direction == 1:
            while y > 0 and array[y - 1][x] != '#':
                if array[y - 1][x] != 'X': unique_locations += 1
                array[y][x] = 'X'
                y -= 1
            if y == 0: return unique_locations + (1 if array[y][x] != 'X' else 0)
            direction = 2


        # >
        if direction == 2:
            while x < len(array[0]) - 1 and array[y][x + 1] != '#':
                if array[y][x + 1] != 'X': unique_locations += 1
                array[y][x] = 'X'
                x += 1
            if x == len(array[0]) - 1: return unique_locations + (1 if array[y][x] != 'X' else 0)
            direction = 3


        # v
        if direction == 3:
            while y < len(array) - 1 and array[y + 1][x] != '#':
                if array[y + 1][x] != 'X': unique_locations += 1
                array[y][x] = 'X'
                y += 1
            if y == len(array) - 1: return unique_locations + (1 if array[y][x] != 'X' else 0)
            direction = 4


        # <
        if direction == 4:
            while x > 0 and array[y][x - 1] != '#':
                if array[y][x - 1] != 'X': unique_locations += 1
                array[y][x] = 'X'
                x -= 1
            if x == 0: return unique_locations + (1 if array[y][x] != 'X' else 0)
            direction = 1



def get_guard_location(array):
    for y in range(len(array) - 1):
        for x, column in enumerate(array[y]):
            if column == "^":
                return x, y
    return -1, -1

if __name__ == "__main__":
    array = get_input(f"src/inputA/{input_path}.txt")
    print(get_unique_locations(array))
