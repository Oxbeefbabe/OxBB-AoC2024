example = open("example.txt", "r")
final = open("final.txt", "r")


def get_power_sum(file):
    power_sum = 0
    for line in file.readlines():
        id, game = get_game_id(line)  # Format the line into an ID and a list containing the rounds of the game
        min_values = {'red': 0, 'green': 0, 'blue': 0}
        for r in game: # Loop through each round in the game
            for colour, num in r:
                min_values[colour] = max(min_values[colour], num) # Update any colours with a new min value if needed
        power_sum += get_power(min_values)
    return power_sum


def get_power(min_values):
    # Given the minimum number of dice needed for a game, get the "power" as described by the elf
    power = 1
    for num in min_values.values():
        power *= num
    return power


def get_game_id(line):
    # Split the game from the ID, and cast ID to int
    id, game_txt = line.split(': ')
    id = int(id.split(' ')[1])

    # Split the rounds apart, and format them into a list containing each colour
    # and the number of cubes that were pulled
    rounds = game_txt.split('; ')
    game = []
    for r in rounds:
        game.append(list(map(lambda value: get_colour_num(value), r.strip().split(', '))))
    return id, game


def get_colour_num(value):
    num, colour = value.split(' ')
    return colour, int(num)


print(f"Example Result: {get_power_sum(example)}")
print(f"Expected Example Result: 2286")
print(f"Actual Test Result: {get_power_sum(final)}")

example.close()
final.close()