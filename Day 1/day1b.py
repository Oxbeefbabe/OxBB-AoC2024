example = open("example_b.txt", "r")
final = open("final.txt", "r")

# Generate the numbers (both integer values and written out strings) we are looking for
NUMS = [str(i) for i in range(1, 10)]
NUM_STRS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"] # 'zero' does not appear in the text


# Pre generate the partial strings of the written out numbers, removing duplicates
# This saves having to constantly regenerate them when processing the text
def gen_partial(i):
    partial = []
    for s in NUM_STRS:
        length = len(s)
        if length == i:
            partial.append(s)
        elif length > i:
            partial.append(s[:i])
    return partial

NUM_STRS_PARTIALS = [gen_partial(i) for i in range(1,6)]


def get_calibration_values(file):
    calibration_values = []

    # Loop through each line
    for line in file.readlines():

        line_nums = []
        # Loop through each character in the line, saving the index (i)
        for i, c in enumerate(line):
            if c in NUMS: line_nums.append(c) # If c is an integer, add it to line_nums
            elif c in NUM_STRS_PARTIALS[0]:
                # If c is the start of a written out number, begin looping through NUM_STRS_PARTIALS
                j = 1
                while True:
                    # If you reach the end of the string, break out of the while loop
                    if len(line) - 1 < i + j + 1: break
                    potential_num = ''.join(line[i: i + j + 1]) # Create a string of the next character in the line
                    if potential_num in NUM_STRS_PARTIALS[j]: # If string appears in NSP, keep looping after this:
                        # If string appears in NUM_STRS, then a written out number was found
                        # Add it to line_nums, and break out of while loop to go to the next character
                        if potential_num in NUM_STRS:
                            line_nums.append(NUMS[NUM_STRS.index(potential_num)])
                            break
                        # Otherwise increment J to get another character next time
                        j += 1
                    else: # If the string doesn't appear in NSP, then break the while loop and move on
                        break


        # Grab first and last line_nums and concat to a string
        calib_str = line_nums[0] + line_nums[-1]

        # Convert string to int to get two digit value
        # Add value to calibration_values list
        calibration_values.append(int(calib_str))
    return calibration_values


print(f"Example Result: {sum(get_calibration_values(example))}")
print(f"Expected Example Result: 281")
print(f"Actual Test Result: {sum(get_calibration_values(final))}")

example.close()
final.close()