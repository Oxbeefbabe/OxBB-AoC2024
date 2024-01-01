example = open("example_a.txt", "r")
final = open("final.txt", "r")

def get_calibration_values(file):
    calibration_values = []
    for line in file.readlines():
        # Remove non-numeric values
        line_nums = list(filter(lambda c: is_numeric(c), line))

        # Grab first and last value and concat to a string
        calib_str = line_nums[0] + line_nums[-1]

        # Convert string to int to get two digit value
        # Add value to calibration_values list
        calibration_values.append(int(calib_str))
    return calibration_values

def is_numeric(c):
    try:
        int(c)
    except ValueError:
        return False
    return True

print(f"Example Result: {sum(get_calibration_values(example))}")
print(f"Expected Example Result: 142")
print(f"Actual Test Result: {sum(get_calibration_values(final))}")

example.close()
final.close()