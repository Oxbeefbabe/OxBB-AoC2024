EXAMPLE = False
input_path = "example" if EXAMPLE else "input"

def get_input(path):
    input_array = []
    with open(path, "r") as file:
        for line in file:
            input_array.append(line.strip())
    return input_array

def search_for_xmas_in(array):
    xmas_count = 0
    for y, column in enumerate(array):
        for x, row in enumerate(array):
            if array[y][x] == 'A' and x >= 1 and y >= 1 and x <= len(array[0]) - 2 and y <= len(array) - 2:
                xmas_count += search_for_xmas_from(x, y, array)
    return xmas_count

def search_for_xmas_from(x, y, array):
    if array[y - 1][x - 1] == "M":
        if array[y - 1][x + 1] == "M":
            if array[y + 1][x - 1] == "S" and array[y + 1][x + 1] == "S":
                return 1
        elif array[y + 1][x - 1] == "M":
            if array[y - 1][x + 1] == "S" and array[y + 1][x + 1] == "S":
                return 1
    elif array[y - 1][x - 1] == "S":
        if array[y - 1][x + 1] == "S":
            if array[y + 1][x - 1] == "M" and array[y + 1][x + 1] == "M":
                return 1
        elif array[y + 1][x - 1] == "S":
            if array[y - 1][x + 1] == "M" and array[y + 1][x + 1] == "M":
                return 1

    return 0



if __name__ == "__main__":
    array = get_input(f"src/inputA/{input_path}.txt")
    print(search_for_xmas_in(array))