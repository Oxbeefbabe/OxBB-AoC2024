example = open("example.txt", "r")
final = open("final.txt", "r")

# The max number of dice as explained by the elf
MAX_VALUES = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def get_possible_sum(file):
    possible_sum = 0
    for line in file.readlines():
        id, game = get_game_id(line) # Format the line into an ID and a list containing the rounds of the game
        possible = True
        for r in game:
            if not possible: break # If not possible break out of the outer loop
            for value in r: # Loop through each round (round is a built-in function of python so 'r' is used)
                if MAX_VALUES[value[0]] < value[1]: # Compare the number of cubes to the maximum number stated
                    possible = False # If not possible break out of inner loop (and later outer loop)
                    break
        possible_sum += id if possible else 0 # If possible, add ID of game to the sum

    return possible_sum


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


print(f"Example Result: {get_possible_sum(example)}")
print(f"Expected Example Result: 8")
print(f"Actual Test Result: {get_possible_sum(final)}")

example.close()
final.close()