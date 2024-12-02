EXAMPLE = False
input_path = "example" if EXAMPLE else "input"


def get_safe_report_count(path):
    safe_report_count = 0
    with open(path, "r") as file:
        for line in file:
            report = list(map(lambda x: int(x), line.strip().split(" ")))
            if is_safe(report): safe_report_count += 1
    return safe_report_count


def is_safe(report, dampener_used=False):
    increasing = report[0] < report[1]
    for index, value in enumerate(report):
        if index == len(report) - 1: return True
        change = report[index + 1] - value
        if change == 0 or abs(change) > 3 or (increasing and change < 0) or ((not increasing) and change > 0):
            if dampener_used: return False
            # Brute force checking all of the potential dampener positions, not very efficient, but I don't have the time to fix it
            return any([is_safe(report[:i] + report[i + 1:], True) for i in range(len(report))])


if __name__ == "__main__":
    print(get_safe_report_count(f"src/inputA/{input_path}.txt"))
