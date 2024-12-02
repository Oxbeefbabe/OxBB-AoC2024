from collections import Counter

EXAMPLE = False
input_path = "example" if EXAMPLE else "input"


def get_input(path):
    list_a = []
    list_b = []
    with open(path, "r") as file:
        for line in file:
            a, b = line.strip().split("   ")
            list_a = binary_insert(list_a, int(a))
            list_b = binary_insert(list_b, int(b))
    return list_a, list_b


def binary_insert(l, num):
    if not l:
        return [num]

    low = 0
    high = len(l) - 1

    while low <= high:
        mid = (high + low) // 2
        if (l[mid] == num) or low == high:
            if num <= l[mid]:
                l.insert(mid, num)
            else:
                l.insert(mid + 1, num)
            return l
        elif l[mid] < num:
            low = mid + 1
        else:
            high = mid - 1

    if num <= l[mid]:
        l.insert(mid, num)
    else:
        l.insert(mid + 1, num)

    return l


def get_similarity(a, b):
    b_count = Counter(b)
    score = 0
    for value in a:
        score += value * b_count[value]

    return score


if __name__ == "__main__":
    list_a, list_b = get_input(f"src/inputA/{input_path}.txt")
    print(get_similarity(list_a, list_b))
