EXAMPLE = True
input_path = "example" if EXAMPLE else "input"


def get_input(path):
    input_text = ""
    with open(path, "r") as file:
        for line in file:
            input_text += line.strip()
    return input_text

def get_uncompressed_file(text):
    uncompressed_file = ""
    free_space = False
    file_id = 0
    for code in text:
        if free_space:
            uncompressed_file += ('.' * int(code))
            free_space = False
        else:
            uncompressed_file += (str(file_id) * int(code))
            file_id += 1
            free_space = True
    return uncompressed_file

if __name__ == "__main__":
    hard_drive = get_input(f"src/inputA/{input_path}.txt")
    print(get_uncompressed_file(hard_drive))