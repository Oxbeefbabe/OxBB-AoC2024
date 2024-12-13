EXAMPLE = True
input_path = "example" if EXAMPLE else "input"


def get_input(path):
    input_text = ""
    with open(path, "r") as file:
        for line in file:
            input_text += line
    return input_text


if __name__ == "__main__":
    print(get_input(f"src/inputB/{input_path}.txt"))