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
            if array[y][x] == 'X':
                xmas_count += search_for_xmas_from(x, y, array)
    return xmas_count

def search_for_xmas_from(x, y, array):
    xmas_count = 0
    # Search Up
    if y >= 3:
        offset = 1
        for letter in "MAS":
            if array[y - offset][x] == letter:
                offset += 1
                if letter == "S": xmas_count += 1
            else: break

    # Search Up-Right
    if y >= 3 and x <= len(array[0]) - 4:
        offset = 1
        for letter in "MAS":
            if array[y - offset][x + offset] == letter:
                offset += 1
                if letter == "S": xmas_count += 1
            else: break

    # Search Right
    if x <= len(array[0]) - 4:
        offset = 1
        for letter in "MAS":
            if array[y][x + offset] == letter:
                offset += 1
                if letter == "S": xmas_count += 1
            else: break

    # Search Down-Right
    if y <= len(array) - 4 and x <= len(array[0]) - 4:
        offset = 1
        for letter in "MAS":
            if array[y + offset][x + offset] == letter:
                offset += 1
                if letter == "S": xmas_count += 1
            else: break

    # Search Down
    if y <= len(array[0]) - 4:
        offset = 1
        for letter in "MAS":
            if array[y + offset][x] == letter:
                offset += 1
                if letter == "S": xmas_count += 1
            else: break

    # Search Down-Left
    if y <= len(array[0]) - 4 and x >= 3:
        offset = 1
        for letter in "MAS":
            if array[y + offset][x - offset] == letter:
                offset += 1
                if letter == "S": xmas_count += 1
            else: break

    # Search Left
    if x >= 3:
        offset = 1
        for letter in "MAS":
            if array[y][x - offset] == letter:
                offset += 1
                if letter == "S": xmas_count += 1
            else: break

    # Search Up-Left
    if y >= 3 and x >= 3:
        offset = 1
        for letter in "MAS":
            if array[y - offset][x - offset] == letter:
                offset += 1
                if letter == "S": xmas_count += 1
            else: break

    return xmas_count



if __name__ == "__main__":
    array = get_input(f"src/inputA/{input_path}.txt")
    print(search_for_xmas_in(array))