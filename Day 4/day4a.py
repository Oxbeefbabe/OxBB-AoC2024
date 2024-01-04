example = open("example.txt", "r")
final = open("final.txt", "r")


def get_scratchcard_points(file):
    points = 0 # Keep track of the number of points we have
    for line in file.readlines():

        # Process the line into two sorted lists of integers, one for the winning numbers, and one for the played
        # numbers on the card. This makes it easier to then process the number of points
        line = line.split(':')[1]
        winning_nums, played_nums = line.strip().split(' | ')
        winning_nums = map(lambda x: 0 if x == '' else int(x), winning_nums.split(' '))
        winning_nums = list(filter(lambda x: x, winning_nums))
        played_nums = map(lambda x: 0 if x == '' else int(x), played_nums.split(' '))
        played_nums = list(filter(lambda x: x, played_nums))
        winning_nums.sort()
        played_nums.sort()

        matches = 0 # Track the number of matches that appear
        current_num = winning_nums.pop(0) # Take the first winning number
        while played_nums: # If we still have played numbers to process
            if current_num < played_nums[0]: # Check if current winning number is smaller than the current played number
                if winning_nums: current_num = winning_nums.pop(0) # If there are any winning numbers left, get another
                else: break # If not, stop looking, as there can be no matches with no winning numbers
            else:
                if current_num == played_nums[0]: matches += 1
                played_nums.pop(0)
        # The points can be determined by calculating 2 to the power of the number of matches - 1
        points += 2**(matches - 1) if matches else 0
    return points


print(f"Example Result: {get_scratchcard_points(example)}")
print(f"Expected Example Result: 13")
print(f"Actual Test Result: {get_scratchcard_points(final)}")

example.close()
final.close()