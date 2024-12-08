EXAMPLE = False
input_path = "example" if EXAMPLE else "input"


def get_input(path):
    rules = {}
    updates = []
    getting_rules = True
    with open(path, "r") as file:
        for line in file:
            if getting_rules:
                if line == "\n":
                    getting_rules = False
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
        for page in update:
            if page in invalid_pages:
                revised_update = fix_update(rules, update)
                page_total += revised_update[len(revised_update) // 2]
                break
            invalid_pages += rules[page] if page in rules else []

    return page_total


def fix_update(rules, update):
    revised_update = [update[0]]
    for page in update[1:]:
        inserted = False
        for pointer, value in enumerate(revised_update):
            if value in rules and page in rules[value]:
                revised_update.insert(pointer, page)
                inserted = True
                break
        if not inserted: revised_update.append(page)

    return revised_update



if __name__ == "__main__":
    rules, updates = get_input(f"src/inputA/{input_path}.txt")
    print(get_valid_updates(rules, updates))
