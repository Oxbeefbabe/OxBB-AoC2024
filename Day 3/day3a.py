example = open("example.txt", "r")
final = open("final.txt", "r")

NUMS = [str(i) for i in range(10)]

def get_schematic_sum(file):
    # Store the schematic
    schematic = []
    for line in file.readlines():
        schematic.append(list(line.strip()))

    # Track the current sum and the height and width of the schematic
    schematic_sum = 0
    height = len(schematic) - 1
    width = len(schematic[0]) - 1

    # Loop through the schematic
    for y, row in enumerate(schematic):
        for x, value in enumerate(row):
            if value not in NUMS and value != '.': # If we run into a symbol, look for any numbers
                # Set the area to search for numbers, making sure to not look over the edge of the schematic
                look_width_start = max(0, x - 1)
                look_width_end = min(width, x + 1)
                look_height_start = max(0, y - 1)
                look_height_end = min(height, y + 1)

                # Loop through the search area
                for i in range(look_height_start, look_height_end + 1):
                    for j in range(look_width_start, look_width_end + 1):
                        if schematic[i][j] in NUMS: # If we find a number:
                            num, new_row = pop_num_at(j, schematic[i]) # Get the number out of the schematic
                            schematic[i] = new_row # Remove it from the schematic (to avoid counting it twice)
                            schematic_sum += num # Add the number to the sum
    return schematic_sum

def pop_num_at(x, row):
    # Find the start/end index's of the number in question
    start = x
    end = x
    while start > -1:
        if row[start] not in NUMS:
            start += 1
            break
        if start == 0:
            break
        start -= 1

    while end < len(row):
        if row[end] not in NUMS:
            break
        end += 1

    num = int(''.join(row[start:end])) # Get the number and convert it to an integer

    # Remove the number from the row to avoid counting it again.
    for i in range(start, end):
        row[i] = '.'
    return num, row # Return the number and the modified row



print(f"Example Result: {get_schematic_sum(example)}")
print(f"Expected Example Result: 4361")
print(f"Actual Test Result: {get_schematic_sum(final)}")

example.close()
final.close()