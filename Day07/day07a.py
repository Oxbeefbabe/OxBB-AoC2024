EXAMPLE = False
input_path = "example" if EXAMPLE else "input"


def get_input(path):
    calibrations = []
    with open(path, "r") as file:
        for line in file:
            line = line.strip().split(":")
            calibrations.append((int(line[0]), list(map(lambda x: int(x), line[1].strip().split()))))
    return calibrations

def get_true_calibrations(calibrations):
    return sum(map(lambda calibration: calibration[0], filter(lambda calibration: calibration_true(calibration), calibrations)))

def calibration_true(calibration):
    result, values = calibration

    if len(values) == 1: return values[0] == result

    if values[0] * values[1] <= result:
        if calibration_true((result, [values[0] * values[1]] + values[2:])):
            return True

    if values[0] + values[1] <= result:
        if calibration_true((result, [values[0] + values[1]] + values[2:])):
            return True

    return False




if __name__ == "__main__":
    cs = get_input(f"src/inputA/{input_path}.txt")
    print(get_true_calibrations(cs))