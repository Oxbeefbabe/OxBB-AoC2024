EXAMPLE = True
input_path = "example" if EXAMPLE else "input"


def get_input(path):
    rules = {}
    updates = []
    getting_rules = True
    with open(path, "r") as file:
        for line in file:
            if getting_rules:
                if line == "\n": getting_rules = False
                else:
                    page2 = int(line.split('|')[0])
                    page1 = int(line.split('|')[1])
                    if page1 in rules:
                        rules[page1] = rules[page1] + [page2]
                    else:
                        rules[page1] = [page2]
            else:
                updates.append(list(map(lambda x: int(x), line.strip().split(','))))
    return rules, updates

def get_valid_updates(rules, updates):
    page_total = 0

    for update in updates:
        invalid_pages = []
        valid = True
        for page in update:
            if page in invalid_pages:
                valid = False
                break
            invalid_pages += rules[page] if page in rules else []
        if valid: page_total += update[len(update) // 2]

    return page_total

if __name__ == "__main__":
    rules, updates = get_input(f"src/inputA/{input_path}.txt")
    print(get_valid_updates(rules, updates))